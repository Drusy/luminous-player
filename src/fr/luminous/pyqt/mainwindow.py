import sys

from PyQt4 import QtGui
from fr.luminous.gmusicapi.gmusic import GMusic
from fr.luminous.utils.auth import Auth
from fr.luminous.utils.time import Time
from fr.luminous.pyqt.ui_mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    gmusic = GMusic(Auth.Login, Auth.Password)
    search_text = ''
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.mainTableWidget.setColumnHidden(0, True)
        
        self.setWindowTitle('Luminous Player')
        self.show()
        
    def init_signals(self):
        # On connected
        self.gmusic.connected_signal.connect(self.on_connected)
        self.gmusic.connected_signal.connect(self.update_all_songs)
        
        # On all song retrieved
        self.gmusic.all_song_signal.connect(self.on_all_songs_updated)
        
        # Main Table Widget
        self.ui.mainTableWidget.itemDoubleClicked.connect(self.on_item_clicked)
        
        # Search edit
        self.ui.searchEdit.editingFinished.connect(self.search)
        
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