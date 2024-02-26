from musicmigrator.common import Platform, Playlist, Track
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List

import urllib.parse

class Spotify(Platform):
    def __init__(self, user_id):
        Platform.__init__(self)
        self.user_id = user_id
        scope = "playlist-modify-public,playlist-modify-private"
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def search_track(self, track:Track, debug=False) -> str:
        """
        Returns the spotify uri of the first found song
        """
        query_strings = [
            f"{track.title} artist:{track.artist} album:{track.album}",
            f"{track.artist} {track.title}"
        ]
        for query in query_strings:
            #query = urllib.parse.quote(query)
            r = self.spotify.search(
                query,
                limit=1,
                type="track",
                market="FR"
            )
            if debug:
                print(r)
            if len(r['tracks']['items']) > 0:
                return r['tracks']['items'][0]['uri']
        return None

    def create_playlist(self, playlist:Playlist):
        """
        Creates a playlist of the given name with the given tracks
        """
        # Search all tracks uris
        uris = []
        for track in playlist:
            uri = self.search_track(track)
            if uri != None:
                print(f"Adding {track} to {playlist}")
                uris.append(uri)
            else:
                print(f"Could not find {track}")
        
        # Create playlist
        pl = self.spotify.user_playlist_create(
            user=self.user_id,
            name=playlist.title
        )

        # Add uris (in order) to the playlist
        frag = 80 # only 80 tracks at a time
        for i in range(0, len(uris), frag):
            self.spotify.user_playlist_add_tracks(
                self.user_id,
                pl['uri'],
                uris[i:i+frag] 
                # note: i+frag overflows but python slices will stop at the end of the list ;)
            )