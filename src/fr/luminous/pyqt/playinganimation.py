from PyQt4 import QtGui, QtCore

class PlayingGif(QtGui.QLabel):
    movie = None
    label = None

    def __init__(self):
        super(PlayingGif, self).__init__()
        
        # Movie
        self.label = QtGui.QLabel()
        self.movie = QtGui.QMovie("./images/equalizer-black.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        
        # Size
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        
        # Layout
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
    def start(self):
        self.movie.start()
        
    def stop(self):
        self.movie.stop()
        