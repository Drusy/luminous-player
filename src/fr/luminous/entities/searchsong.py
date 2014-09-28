class SearchSong(object):
    id = None
    album = None
    genre = None
    play_count = 0
    artist = None
    duration = None
    rating = '0'
    album_cover_url = None
    title = None

    def __init__(self, song_json):
        song_json = song_json.get('track')
        
        self.id = song_json.get('nid', 'unknown')
        self.album = song_json.get('album', 'unknown')
        self.title = song_json.get('title', 'unknown')
        self.genre = song_json.get('genre', 'unknown')
        self.artist = song_json.get('artist', 'unknown')
        self.duration = song_json.get('durationMillis', '0')
        
        album_art_ref = song_json.get('albumArtRef', [])
        first = album_art_ref[0] if album_art_ref else None
        if first != None:
            self.album_cover_url = first.get('url', 'unknown')
        