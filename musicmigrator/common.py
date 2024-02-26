from typing import List
import os
from colorama import Fore

class Track:
    def __init__(self, artist:str, title:str, album=""):
        self.artist = artist
        self.title = title
        self.album = album
    def __repr__(self):
        return f"<Track {Fore.CYAN}{self.artist}{Fore.RESET} : {Fore.MAGENTA}{self.title}{Fore.RESET}>"

class Playlist:
    def __init__(self, title:str, tracks:List[Track]):
        self.title = title
        self.tracks = tracks
    def __iter__(self):
        return iter(self.tracks)
    def __repr__(self):
        return f"{Fore.GREEN}{self.title}{Fore.RESET}"

class Platform:
    """
    Generic model to interact with a platform (spotify, deezer, ...)
    """
    def __init__(self, *args, **kwargs):
        # Environment variables required to interact with the platfrom
        self.required_env = []

        for key in self.required_env:
            val = os.getenv(key)
            if val == None:
                print(f"{Fore.YELLOW}Warning !{Fore.RESET} : {key} is missing from the environment")

    def auth(self):
        """
        Authenticate with the platform
        """
        1
    # Read functions
    def get_playlists(self):
        1
    def get_playlist(self, playlist_obj_or_id) -> List[Track]:
        1
    def search_track(self, track:Track) -> object:
        """
        Returns the track identifier specific to the platform, eg: spotify has a string format : spotify:track:7FCf3MkIYtZw7FZizebsZY
        """
        1
    def create_playlist(self, playlist:List[object]):
        """
        Create the playlist using a list of track identifiers specific to the platform 
        """
        1