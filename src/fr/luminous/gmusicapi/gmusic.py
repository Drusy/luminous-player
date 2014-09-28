# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, pyqtSignal, QFile
from fr.luminous.utils.config import Config
from gmusicapi import Webclient
from gmusicapi import Mobileclient
from gmusicapi.utils import utils

class GMusic(QThread):
    login = ''
    password = ''
    thread_starter = 'connect'
    thread_args = ''
    web_client = Webclient()
    mobile_client = Mobileclient()
    
    # Signals 
    connected_signal = pyqtSignal(bool)
    all_song_signal = pyqtSignal(list)
    play_song_signal = pyqtSignal(str, str)
    search_result_signal = pyqtSignal(dict)

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
    
    def search_all_access(self, query, max_results = 100):
        return self.mobile_client.search_all_access(unicode(query), max_results)
        
    def download_song(self, song_id, filename):
        mp3_file = QFile(filename)
        
        if mp3_file.exists():
            print("Song already %s exists in cache" % (song_id))
        else:
            print("Downloading song %s to %s " % (song_id, filename))
            
            mp3_data = self.get_stream_audio(str(song_id))
            with open(filename, 'wb') as music_file:
                music_file.write(mp3_data)

    def download_and_play_song(self, song_id, filename):
        file_path = "%s/%s" % (Config.get_music_storage_folder(), filename)
        self.download_song(song_id, file_path)
        self.play_song_signal.emit(file_path, song_id)
        
    def on_volume_changed(self, volume):
        self.volume = volume
        if self.current_clip != None:
            self.current_clip.stop()
            self.current_clip.volume(volume)
            self.current_clip.play()
        
    def run(self):
        if self.thread_starter == 'connect':
            connected = self.do_login(self.login, self.password)
            self.connected_signal.emit(connected)
            
        if self.thread_starter == 'disconnect':
            self.do_logout()
            
        if self.thread_starter == 'all_songs':
            all_songs = self.get_all_songs()
            self.all_song_signal.emit(all_songs)
            
        if self.thread_starter == 'search':
            search_result = self.search_all_access(self.thread_args)
            self.search_result_signal.emit(search_result)
            
        if self.thread_starter == 'down_play':
            self.download_and_play_song(self.thread_args, "%s.mp3" % self.thread_args)
    
    def start_in_thread(self, starter_value, args = ''):
        self.thread_args = args
        self.thread_starter = starter_value
        self.start()
        
