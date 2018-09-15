import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='20d4f81cf8c8467a9b85ddd72befa1ae',
                                                      client_secret='73a59aea79894cdca9acb09541dfae76')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_track(track):
    track_id = spotify.search(track, type='track')
    return (track_id["tracks"]["items"][0]['external_urls'])

print (search_track("despacito"))