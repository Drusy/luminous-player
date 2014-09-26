import mp3play

from PyQt4.QtCore import QThread, pyqtSignal
from gmusicapi import Webclient
from gmusicapi import Mobileclient
from gmusicapi.utils import utils

class GMusic(QThread):
    login = ''
    password = ''
    thread_starter = 'connect'
    web_client = Webclient()
    mobile_client = Mobileclient()
    
    # Signals 
    connected_signal = pyqtSignal(bool)
    all_song_signal = pyqtSignal(list)

    def __init__(self, login, password):
        super(GMusic, self).__init__()
        
        self.login = login
        self.password = password
        
        print("GMusic thread initialized")
        print("Log file : %s" % utils.log_filepath)
        
    def do_login(self, login, password):
        web_client_state = self.web_client.login(login, password)
        mobile_client_state = self.mobile_client.login(login, password)
        
        print("Logged in to web client : %s" % web_client_state)
        print("Logged in to mobile client : %s" % mobile_client_state)
        
        return (mobile_client_state and web_client_state)
    
    def do_logout(self):
        self.web_client.logout()
        self.mobile_client.logout()
        print("Logged out")
        
    def get_song_download_info(self, song_id):
        return self.web_client.get_song_download_info(song_id)
    
    def get_registered_devices(self):
        return self.web_client.get_registered_devices()
    
    def get_stream_audio(self, song_id):
        return self.web_client.get_stream_audio(song_id)
    
    def get_all_songs(self, incremental=False, include_deleted=False):
        return self.mobile_client.get_all_songs(incremental, include_deleted)
    
    def search_all_access(self, query, max_results):
        return self.mobile_client.search_all_access(query, max_results)
    
    def play_song(self, filename):
        clip = mp3play.load(filename)
        clip.play()
        
    def download_song(self, song_id, filename):
        mp3_data = self.get_stream_audio(song_id)
        
        with open(filename, 'wb') as music_file:
            music_file.write(mp3_data)
            
    def download_and_play_song(self, song_id, filename):
        self.download_song(song_id, filename)
        self.play_song(filename)
        
    def run(self):
        if self.thread_starter == 'connect':
            connected = self.do_login(self.login, self.password)
            self.connected_signal.emit(connected)
        if self.thread_starter == 'disconnect':
            self.do_logout()
        if self.thread_starter == 'all_songs':
            all_songs = self.get_all_songs()
            self.all_song_signal.emit(all_songs)
    
    def start_in_thread(self, starter_value):
        self.thread_starter = starter_value
        self.start()
        
