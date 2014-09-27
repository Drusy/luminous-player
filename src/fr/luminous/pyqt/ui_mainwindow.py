from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1040, 652)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchEdit = QtGui.QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.userLogin = QtGui.QLabel(self.centralwidget)
        self.userLogin.setObjectName(_fromUtf8("userLogin"))
        self.horizontalLayout.addWidget(self.userLogin)
        self.userIcon = QtGui.QLabel(self.centralwidget)
        self.userIcon.setObjectName(_fromUtf8("userIcon"))
        self.horizontalLayout.addWidget(self.userIcon)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.verticalWidget_2.setObjectName(_fromUtf8("verticalWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.leftMenu = QtGui.QListWidget(self.verticalWidget_2)
        self.leftMenu.setObjectName(_fromUtf8("leftMenu"))
        self.verticalLayout_5.addWidget(self.leftMenu)
        self.leftPlaylist = QtGui.QListWidget(self.verticalWidget_2)
        self.leftPlaylist.setObjectName(_fromUtf8("leftPlaylist"))
        self.verticalLayout_5.addWidget(self.leftPlaylist)
        self.horizontalLayout_4.addWidget(self.verticalWidget_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.songSelectionButton = QtGui.QPushButton(self.centralwidget)
        self.songSelectionButton.setObjectName(_fromUtf8("songSelectionButton"))
        self.horizontalLayout_5.addWidget(self.songSelectionButton)
        self.artistsSelectionButton = QtGui.QPushButton(self.centralwidget)
        self.artistsSelectionButton.setObjectName(_fromUtf8("artistsSelectionButton"))
        self.horizontalLayout_5.addWidget(self.artistsSelectionButton)
        self.albumsSelectionButton = QtGui.QPushButton(self.centralwidget)
        self.albumsSelectionButton.setObjectName(_fromUtf8("albumsSelectionButton"))
        self.horizontalLayout_5.addWidget(self.albumsSelectionButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.shuffleLibraryButton = QtGui.QPushButton(self.centralwidget)
        self.shuffleLibraryButton.setObjectName(_fromUtf8("shuffleLibraryButton"))
        self.horizontalLayout_5.addWidget(self.shuffleLibraryButton)
        self.uploadMusicButton = QtGui.QPushButton(self.centralwidget)
        self.uploadMusicButton.setObjectName(_fromUtf8("uploadMusicButton"))
        self.horizontalLayout_5.addWidget(self.uploadMusicButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.mainTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.mainTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mainTableWidget.setProperty("showDropIndicator", False)
        self.mainTableWidget.setAlternatingRowColors(True)
        self.mainTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.mainTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.mainTableWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.mainTableWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.mainTableWidget.setShowGrid(False)
        self.mainTableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.mainTableWidget.setCornerButtonEnabled(False)
        self.mainTableWidget.setObjectName(_fromUtf8("mainTableWidget"))
        self.mainTableWidget.setColumnCount(7)
        self.mainTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(6, item)
        self.mainTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.mainTableWidget.horizontalHeader().setHighlightSections(False)
        self.mainTableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.mainTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.mainTableWidget.horizontalHeader().setStretchLastSection(True)
        self.mainTableWidget.verticalHeader().setVisible(False)
        self.mainTableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.mainTableWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.trackIcon = QtGui.QLabel(self.centralwidget)
        self.trackIcon.setObjectName(_fromUtf8("trackIcon"))
        self.horizontalLayout_2.addWidget(self.trackIcon)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.musicSeeker = QtGui.QSlider(self.centralwidget)
        self.musicSeeker.setOrientation(QtCore.Qt.Horizontal)
        self.musicSeeker.setObjectName(_fromUtf8("musicSeeker"))
        self.verticalLayout_3.addWidget(self.musicSeeker)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.trackName = QtGui.QLabel(self.centralwidget)
        self.trackName.setAlignment(QtCore.Qt.AlignCenter)
        self.trackName.setObjectName(_fromUtf8("trackName"))
        self.verticalLayout_2.addWidget(self.trackName)
        self.trackArtist = QtGui.QLabel(self.centralwidget)
        self.trackArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.trackArtist.setObjectName(_fromUtf8("trackArtist"))
        self.verticalLayout_2.addWidget(self.trackArtist)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(75, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.loopButton = QtGui.QPushButton(self.centralwidget)
        self.loopButton.setObjectName(_fromUtf8("loopButton"))
        self.horizontalLayout_3.addWidget(self.loopButton)
        self.prevButton = QtGui.QPushButton(self.centralwidget)
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.horizontalLayout_3.addWidget(self.prevButton)
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout_3.addWidget(self.playButton)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout_3.addWidget(self.nextButton)
        self.randomButton = QtGui.QPushButton(self.centralwidget)
        self.randomButton.setObjectName(_fromUtf8("randomButton"))
        self.horizontalLayout_3.addWidget(self.randomButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.soundSeeker = QtGui.QSlider(self.centralwidget)
        self.soundSeeker.setMaximum(100)
        self.soundSeeker.setProperty("value", 100)
        self.soundSeeker.setOrientation(QtCore.Qt.Horizontal)
        self.soundSeeker.setObjectName(_fromUtf8("soundSeeker"))
        self.horizontalLayout_3.addWidget(self.soundSeeker)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Luminous Player", None))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "Search music", None))
        self.userLogin.setText(_translate("MainWindow", "kevin.renella@gmail.com", None))
        self.userIcon.setText(_translate("MainWindow", "User Icon", None))
        self.songSelectionButton.setText(_translate("MainWindow", "Songs", None))
        self.artistsSelectionButton.setText(_translate("MainWindow", "Artists", None))
        self.albumsSelectionButton.setText(_translate("MainWindow", "Albums", None))
        self.shuffleLibraryButton.setText(_translate("MainWindow", "Shuffle Library", None))
        self.uploadMusicButton.setText(_translate("MainWindow", "Upload Music", None))
        self.mainTableWidget.setSortingEnabled(True)
        item = self.mainTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id", None))
        item = self.mainTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.mainTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.mainTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Artist", None))
        item = self.mainTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Album", None))
        item = self.mainTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Count", None))
        item = self.mainTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Rating", None))
        self.trackIcon.setText(_translate("MainWindow", "Track Icon", None))
        self.trackName.setText(_translate("MainWindow", "Track Name", None))
        self.trackArtist.setText(_translate("MainWindow", "Artist - Album", None))
        self.loopButton.setText(_translate("MainWindow", "Loop", None))
        self.prevButton.setText(_translate("MainWindow", "Prev", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.randomButton.setText(_translate("MainWindow", "Random", None))
        self.pushButton_3.setText(_translate("MainWindow", "Rating Up", None))
        self.pushButton_4.setText(_translate("MainWindow", "Rating Down", None))
