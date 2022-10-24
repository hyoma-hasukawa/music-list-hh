from pprint import pprint
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def index(request):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    resulta = current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    # current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
    # featured_playlists(locale=None, country=None, timestamp=None, limit=20, offset=0)
    return render(request,"artist/index.html")


# client id =da5b39a37d8d422e9f22d5c05a7a56e6
# アルバム名を取ってきている。（）
    # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    # results = spotify.artist_albums(birdy_uri, album_type='album')
    # albums = results['items']
    # while results['next']:
    #     results = spotify.next(results)
    #     albums.extend(results['items'])

    # for album in albums:
    #     print(album['name'])


# カバーアートと音楽を載せている。
    # lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    # results = spotify.artist_top_tracks(lz_uri)

    # for track in results['tracks'][:10]:
    #     print('track    : ' + track['name'])
    #     print('audio    : ' + track['preview_url'])
    #     print('cover art: ' + track['album']['images'][0]['url'])
    #     print()


# 授業の時の
    # lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
    # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    # resulta = spotify.artist_top_tracks(lz_uri)
    # pprint(resulta)

    # results=spotify.search("kick" ,type="album")
    # pprint(results)


    # scope = "user-library-read"

    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # results = sp.current_user_saved_tracks()
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])

