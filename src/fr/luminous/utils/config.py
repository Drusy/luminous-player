from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QDir

class Config(object):
    Height = 300
    Width = 300
    DataPrefix = '/luminous'
    MusicPrefix = '/library'
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_music_storage_folder():  
        storage_path = "%s%s%s" % (QDesktopServices.storageLocation(QDesktopServices.DataLocation).replace("\\", "/"), Config.DataPrefix, Config.MusicPrefix)
        dir = QDir(storage_path)
        
        if dir.exists() != True:
            dir.mkpath('.')
        
        return storage_path