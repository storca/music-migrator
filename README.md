# MusicMigrator

Migrate your playlists between streaming platforms, without giving away your data to third-parties.

## Setup

Install dependencies
```bash
pip install -r requirements.txt
```

Copy file template, edit it and add the variables to the current environment
```bash
cp env.example.sh env.sh
gedit env.sh
source env.sh
```

## Usage
Note : **Only Deezer to Spotify is supported at the moment**

### Deezer to spotify

* Gather your playlist ids from your deezer account, it is an integer that you find in the URL
* Get your user id from spotify by browsing to your profile and taking it from the url, it is a string of numbers and letters
* Run the script, log in once to your spotify account and watch the playlist migrate

```bash
python deezer_to_spotify.py
```


## Features (per platform)

### Spotify

* Automated OAUTH using spotipy
* Search using multiple search queries if one fails
* Supports big playlists (>100 tracks)

TODO : fetch playlists from user profile

### Deezer

* Retrieve tracks from public playlists, using playlist ids

TODO : OAUTH, search tracks and create playlists

## Project state

For now only Deezer to Spotify is supported (full deezer account to blank spotify account).
More features can be implemented following the ```Platform``` class in ```common.py```.


