from musicmigrator.common import Track, Platform, Playlist
from deezer import Client

class Deezer(Platform):
    def __init__(self):
        Platform.__init__(self)
        self.can_retrieve_user_playlists = False
        self.requires_auth = False

        self.client = Client()

    def get_playlist(self, playlist_id:int) -> Playlist:
        playlist = self.client.get_playlist(playlist_id)
        tracks = []
        for t in playlist.tracks:
            tracks.append(
                Track(t.artist.name, t.title, t.album.title)
            )
        return Playlist(playlist.title, tracks)

    # TODO, with python oauth
    def create_playlist(playlist:Playlist):
        1