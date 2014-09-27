import sys
import mp3play
import threading

from PyQt4 import QtGui
from fr.luminous.gmusicapi.gmusic import GMusic
from fr.luminous.utils.auth import Auth
from fr.luminous.utils.time import Time
from fr.luminous.pyqt.ui_mainwindow import Ui_MainWindow
from sched import scheduler
from PyQt4.Qt import QApplication

class MainWindow(QtGui.QMainWindow):
    gmusic = GMusic(Auth.Login, Auth.Password)
    search_text = ''
    current_mp3 = None
    volume = 100
    should_timer_run = True
    current_track_seeker = 0
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # UI
        self.init_ui()
        self.init_signals()
        
    def check_second(self):
        if self.current_mp3 != None and self.should_timer_run == True:
            self.current_track_seeker += 1
            if self.ui.musicSeeker.isSliderDown() == False:
                self.ui.musicSeeker.setValue(self.current_track_seeker)

            threading.Timer(1, self.check_second).start (); 

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.mainTableWidget.setColumnHidden(0, True)
        self.ui.soundSeeker.setValue(self.volume)
        
        self.setWindowTitle('Luminous Player')
        self.show()
        
    def closeEvent(self,event):
        self.should_timer_run = False
        
    def on_volume_changed(self, value):
        if self.current_mp3 != None:
            self.current_mp3.volume(value)
        
    def init_signals(self):
        # gmusic
        self.gmusic.connected_signal.connect(self.on_connected)
        self.gmusic.connected_signal.connect(self.update_all_songs)
        self.gmusic.all_song_signal.connect(self.on_all_songs_updated)
        self.gmusic.play_song_signal.connect(self.on_play_song)
        
        # UI
        self.ui.mainTableWidget.itemDoubleClicked.connect(self.on_item_clicked)
        self.ui.searchEdit.editingFinished.connect(self.search)
        self.ui.soundSeeker.valueChanged.connect(self.on_volume_changed)
        self.ui.playButton.clicked.connect(self.on_play_clicked)
        self.ui.musicSeeker.sliderReleased.connect(self.on_music_slider_released)
        self.ui.musicSeeker.valueChanged.connect(self.on_music_slider_value_changed)
        
    def on_play_song(self, filename):
        self.ui.playButton.setText("Pause")
        if self.current_mp3 != None:
            self.current_mp3.stop()
        
        self.current_mp3 = mp3play.load(filename)
        self.current_mp3.play()
        self.current_mp3.volume(self.volume)
        
        self.ui.musicSeeker.setValue(0)
        self.current_track_seeker = 0
        self.check_second()
        self.ui.musicSeeker.setMaximum(self.current_mp3.seconds())
        
        print("Playing song %s (%d secs)" % (filename, self.current_mp3.seconds()))
        
    def on_stop_song(self):
        self.ui.playButton.setText("Play")
        self.should_timer_run = False
        if self.current_mp3 != None:
            self.current_mp3.stop()
            
    def on_music_slider_value_changed(self, value):
        if value == self.ui.musicSeeker.maximum():
            self.on_stop_song()
        
    def on_music_slider_released(self):
        paused = self.current_mp3.ispaused()
        value = self.ui.musicSeeker.value()
        
        if self.current_mp3 != None:
            self.current_track_seeker = value
            self.current_mp3.play(value * 1000)
            
            if paused == True:
                self.current_mp3.pause()
        
    def on_play_clicked(self):
        if self.current_mp3 != None:
            # Pause
            if self.current_mp3.isplaying():
                self.ui.playButton.setText("Play")
                self.current_mp3.pause()
                self.should_timer_run = False
            # Unpause
            else:
                self.ui.playButton.setText("Pause")
                self.current_mp3.unpause()
                self.should_timer_run = True
                self.check_second()
        else:
            current = self.ui.mainTableWidget.currentItem()
            # Row selected, start player
            if current != None:
                self.on_item_clicked(current)
            # Should start random track ?
            else:
                pass
            
        
    def on_item_clicked(self, table_item):
        row = table_item.row()
        music_id = self.ui.mainTableWidget.item(row, 0).text()
        self.gmusic.start_in_thread('down_play', music_id)

    def on_all_songs_updated(self, all_songs):
        i = 0
        
        self.ui.mainTableWidget.clearContents()

        for song in all_songs:
            self.ui.mainTableWidget.insertRow(i)
            
            self.ui.mainTableWidget.setItem(i, 0, QtGui.QTableWidgetItem(song['id']))
            self.ui.mainTableWidget.setItem(i, 1, QtGui.QTableWidgetItem(song['title']))
            self.ui.mainTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(Time.millis_to_string(song['durationMillis'])))
            self.ui.mainTableWidget.setItem(i, 3, QtGui.QTableWidgetItem(song['artist']))
            self.ui.mainTableWidget.setItem(i, 4, QtGui.QTableWidgetItem(song['album']))
            self.ui.mainTableWidget.setItem(i, 5, QtGui.QTableWidgetItem(str(song.get('playCount', '0'))))
            self.ui.mainTableWidget.setItem(i, 6, QtGui.QTableWidgetItem(song.get('rating', '0')))
            
            i += 1
            
    def search(self):
        if self.ui.searchEdit.text() != self.search_text:
            self.search_text = self.ui.searchEdit.text()
            if self.ui.searchEdit.text() != '':
                self.gmusic.start_in_thread('search', self.ui.searchEdit.text())
            
    def on_connected(self, connected):
        if connected == True:
            self.ui.userLogin.setText(Auth.Login)
        else:
            self.ui.userLogin.setText("Connection failed")
        
    def init_gmusic_data(self):
        self.gmusic.start_in_thread('connect')
        
    def update_all_songs(self):
        self.gmusic.start_in_thread('all_songs')
        
def main():
    app = QtGui.QApplication(sys.argv)
    
    window = MainWindow()
    window.init_gmusic_data()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()