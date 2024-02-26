from musicmigrator.platforms import Deezer
from musicmigrator.platforms import Spotify

playlist = input("Enter your deezer playlist id (found in the url) : ")
spotify_user_id = input("Enter your spotify user id (found in the url) : ")

d = Deezer()
pl = d.get_playlist(int(playlist))

s = Spotify(spotify_user_id)
s.create_playlist(pl)