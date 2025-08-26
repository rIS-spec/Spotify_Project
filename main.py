import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# Search for Arijit Singh and get his artist URI
results = sp.search(q='Arijit Singh', type='artist')
artist_uri = results['artists']['items'][0]['uri']

# Get albums by Arijit Singh, filtering only 'album' type (official albums)
albums = sp.artist_albums(artist_uri, album_type='album', country='IN')  # country='IN' for India

# Use a set to avoid duplicate albums
album_names = set()

print("Official Albums by Arijit Singh:\n")

for album in albums['items']:
    # Filter out compilations or albums that are not official
    if album['album_type'] == 'album':
        album_name = album['name']
        if album_name not in album_names:
            album_names.add(album_name)
            print(f"Album: {album_name}")

            # Get tracks in this album
            tracks = sp.album_tracks(album['id'])
            for track in tracks['items']:
                print(f"  - {track['name']}")
            print()  # Blank line between albums
