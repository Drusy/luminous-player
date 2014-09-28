class Song(object):
    id = None
    album = None
    deleted = None
    genre = None
    play_count = None
    artist = None
    duration = None
    rating = None
    album_cover_url = None
    title = None

    def __init__(self, song_json):
        self.id = song_json.get('id', 'unknown')
        self.album = song_json.get('album', 'unknown')
        self.title = song_json.get('title', 'unknown')
        self.deleted = song_json.get('deleted', False)
        self.genre = song_json.get('genre', 'unknown')
        self.play_count = song_json.get('playCount', 0)
        self.artist = song_json.get('artist', 'unknown')
        self.duration = song_json.get('durationMillis', '0')
        self.rating = song_json.get('rating', '0')
        
        album_art_ref = song_json.get('albumArtRef', [])
        first = album_art_ref[0] if album_art_ref else None
        if first != None:
            self.album_cover_url = first.get('url', 'unknown')
        