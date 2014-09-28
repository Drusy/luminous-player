# -*- coding: utf-8 -*-

import sys
import hashlib
import mp3play
import urllib
import threading

from PyQt4 import QtGui, QtCore
from fr.luminous.gmusicapi.gmusic import GMusic
from fr.luminous.utils.auth import Auth
from fr.luminous.utils.time import Time
from fr.luminous.pyqt.ui_mainwindow import Ui_MainWindow
from fr.luminous.entities.song import Song
from fr.luminous.entities.searchsong import SearchSong
from fr.luminous.pyqt.loadinganimation import LoadingGif
from fr.luminous.pyqt.playinganimation import PlayingGif

class MainWindow(QtGui.QMainWindow):
    gmusic = GMusic(Auth.Login, Auth.Password)
    search_text = ''
    current_mp3 = None
    volume = 100
    should_timer_run = True
    current_track_seeker = 0
    playing_state = False
    all_songs_list = {}
    search_songs_list = {}
    movie = None
    current_row = None
    current_table = None
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # UI
        self.init_ui()
        self.init_signals()
            
        # Timer
        self.check_second()
        
    def check_second(self):
        if self.current_mp3 != None and self.playing_state == True:
            self.current_track_seeker += 1
            if self.ui.musicSeeker.isSliderDown() == False:
                self.ui.musicSeeker.setValue(self.current_track_seeker)

        if self.should_timer_run == True:
            threading.Timer(1, self.check_second).start (); 

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.soundSeeker.setValue(self.volume)
        self.set_table_column_size(self.ui.allSongsTable)
        self.set_table_column_size(self.ui.searchSongsTable)
        
        self.setWindowTitle('Luminous Player')
        self.show()
        
    def set_table_column_size(self, table):
        table.setColumnHidden(0, True)
        table.horizontalHeader().resizeSection(1, 60);
        table.horizontalHeader().resizeSection(2, 200);
        table.horizontalHeader().resizeSection(3, 50);
        table.horizontalHeader().resizeSection(4, 200);
        table.horizontalHeader().resizeSection(5, 200);
        table.horizontalHeader().resizeSection(6, 50);
        table.horizontalHeader().resizeSection(7, 50);
        
        
    def closeEvent(self,event):
        self.should_timer_run = False
        
    def on_left_menu_item_clicked(self, item):
        selected_row = self.ui.leftMenu.row(item)
        self.ui.stackedWidget.setCurrentIndex(selected_row)
        
    def on_volume_changed(self, value):
        if self.current_mp3 != None:
            self.current_mp3.volume(value)
        
    def init_signals(self):
        # gmusic
        self.gmusic.connected_signal.connect(self.on_connected)
        self.gmusic.connected_signal.connect(self.update_all_songs)
        self.gmusic.all_song_signal.connect(self.on_all_songs_updated)
        self.gmusic.play_song_signal.connect(self.on_play_song)
        self.gmusic.search_result_signal.connect(self.on_search_song_updated)
        
        # UI
        self.ui.allSongsTable.itemDoubleClicked.connect(self.on_item_clicked)
        self.ui.searchSongsTable.itemDoubleClicked.connect(self.on_item_clicked)
        self.ui.searchEdit.editingFinished.connect(self.search)
        self.ui.soundSeeker.valueChanged.connect(self.on_volume_changed)
        self.ui.playButton.clicked.connect(self.on_play_clicked)
        self.ui.musicSeeker.sliderReleased.connect(self.on_music_slider_released)
        self.ui.musicSeeker.valueChanged.connect(self.on_music_slider_value_changed)
        self.ui.leftMenu.itemClicked.connect(self.on_left_menu_item_clicked)
        
    def on_play_song(self, filename, song_id):
        # Stop current track
        self.stop_current_track()
        
        # UI / Pause / Animation
        self.ui.playButton.setText("Pause")
        self.playing_animation(self.current_row)
        
        # Play new track
        self.current_mp3 = mp3play.load(filename)
        self.current_mp3.play()
        self.current_mp3.volume(self.volume)
        
        self.playing_state = True
        self.ui.musicSeeker.setValue(0)
        self.current_track_seeker = 0
        self.ui.musicSeeker.setMaximum(self.current_mp3.seconds())
        
        # Meta data
        self.update_song_data(song_id)
        
        print("Playing song %s (%d secs)" % (filename, self.current_mp3.seconds()))
        
    def playing_animation(self, row):
        table = self.get_current_table()
                    
        table.setCellWidget(row, 1, PlayingGif())
        
    def loading_animation(self, row):
        table = self.get_current_table()
                    
        table.setCellWidget(row, 1, LoadingGif())
        
    def stop_current_track(self):
        if self.current_mp3 != None:
            self.current_mp3.stop()
        self.playing_state = False
        
        if self.current_row != None and self.current_table != None:
            self.current_table.removeCellWidget(self.current_row, 1)
        
    def update_song_data(self, song_id):
        song = self.all_songs_list.get(str(song_id), None)
        if song == None:
            song = self.search_songs_list[str(song_id)]
            
        pixmap = QtGui.QPixmap()
        
        self.ui.trackName.setText(song.title)
        self.ui.trackArtist.setText(song.artist)
        
        if song.album_cover_url != None and song.album_cover_url != 'unknown':
            data = urllib.urlopen(song.album_cover_url).read()
            if pixmap.loadFromData(data):
                self.ui.trackIcon.setPixmap(pixmap)
                return
            
        pixmap.load(":/images/default-album-art.png")
        
    def on_stop_song(self):
        self.ui.playButton.setText("Play")
        self.playing_state = False
        if self.current_mp3 != None:
            self.current_mp3.stop()
            
    def set_gravatar(self):
        hash_email = hashlib.md5(Auth.Login).hexdigest()
        gravatar_url = 'http://www.gravatar.com/avatar/%s?s=30' % hash_email
        data = urllib.urlopen(gravatar_url).read()
        pixmap = QtGui.QPixmap()
        
        if pixmap.loadFromData(data):
            self.ui.userIcon.setPixmap(pixmap)
            
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
                self.playing_state = False
            # Unpause
            else:
                self.ui.playButton.setText("Pause")
                self.current_mp3.unpause()
                self.playing_state = True
        else:
            current = self.ui.allSongsTable.currentItem()
            # Row selected, start player
            if current != None:
                self.on_item_clicked(current)
            # Should start random track ?
            else:
                pass
            
    def get_current_table(self):
        table = None
        
        if self.ui.stackedWidget.currentIndex() == 0:
            table = self.ui.allSongsTable
        elif self.ui.stackedWidget.currentIndex() == 1:
            table = self.ui.searchSongsTable
            
        return table
        
    def on_item_clicked(self, table_item):
        table = self.get_current_table()
        
        # Get row
        row = table_item.row()
        music_id = table.item(row, 0).text() 
        
        # Stop current track
        self.stop_current_track()
        
        # Animation
        self.loading_animation(row)
        self.current_row = row
        self.current_table = table
        
        # Download Music
        self.gmusic.start_in_thread('down_play', music_id)

    def on_all_songs_updated(self, all_songs):
        self.all_songs_list.clear()
        self.ui.leftMenu.setCurrentRow(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        
        for json_song in all_songs:
            song = Song(json_song)
            self.all_songs_list[song.id] = song
            
        self.fill_table(self.ui.allSongsTable, self.all_songs_list)
        
    def on_search_song_updated(self, search_songs):
        search_songs = search_songs.get('song_hits', [])
        self.search_songs_list.clear()
        self.ui.leftMenu.setCurrentRow(1)
        self.ui.stackedWidget.setCurrentIndex(1)
        
        for json_song in search_songs:
            search_song = SearchSong(json_song)
            self.search_songs_list[search_song.id] = search_song
            
        self.fill_table(self.ui.searchSongsTable, self.search_songs_list)
            
    def fill_table(self, table, song_dict):
        i = 0
        
        for table_index in range(0, table.rowCount()):
            table.removeRow(0)
        table.clearContents()

        for song in song_dict.itervalues():
            table.insertRow(i)
            table.setItem(i, 0, QtGui.QTableWidgetItem(song.id))                    
            table.setItem(i, 2, QtGui.QTableWidgetItem(song.title))
            table.setItem(i, 3, QtGui.QTableWidgetItem(Time.millis_to_string(song.duration)))
            table.setItem(i, 4, QtGui.QTableWidgetItem(song.artist))
            table.setItem(i, 5, QtGui.QTableWidgetItem(song.album))
            table.setItem(i, 6, QtGui.QTableWidgetItem(str(song.play_count)))
            table.setItem(i, 7, QtGui.QTableWidgetItem(song.rating))
            
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
        
        self.set_gravatar()
        
    def init_gmusic_data(self):
        self.ui.userIcon.setMovie(LoadingGif().movie)
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
