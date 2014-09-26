import sys

from PyQt4 import QtGui
from fr.luminous.gmusicapi.gmusic import GMusic
from fr.luminous.utils.auth import Auth
from fr.luminous.pyqt.ui_mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    gmusic = GMusic(Auth.Login, Auth.Password)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle('Luminous Player')
        self.show()
        
    def init_signals(self):
        # On connected
        self.gmusic.connected_signal.connect(self.on_connected)
        self.gmusic.connected_signal.connect(self.update_all_songs)
        
        # On all song retrieved
        self.gmusic.all_song_signal.connect(self.update_all_songs_list)

    def update_all_songs_list(self, all_songs):
        for song in all_songs:
            self.ui.listWidget.addItem("%s - %s (%s)" % (song['artist'], song['title'], song['id'])) 
            
    def on_connected(self, connected):
        if connected == True:
            self.ui.label.setText("Connected as %s" % Auth.Login)
        else:
            self.ui.label.setText("Connection failed")
        
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