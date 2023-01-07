# -*- coding: utf-8 -*-
import sys
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.db.models import Q


# inputから検索結果を持ってくる
def index(request):
    query = request.GET.get('search')
    
    # query（入力内容）が存在する場合
    if query:
        # query（入力内容）をspotifyに検索する
        client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6' 
        client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        keyword = query
        results = sp.search(q=keyword, limit=10, market="JP")

        for idx, track in enumerate(results['tracks']['items']):
            print(idx + 1, track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()
        # query（入力内容）が存在しない場合
        else:
            print(idx)
            # return render(request,"mypage/index.html")
    
    # else:
    #     posts = Post.objects.all().order_by('-created_at')  
    # return render(request, 'blog_app/index.html', {'posts': posts, 'query': query,})



# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'


# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
#入力パート
# artist_url = 'https://open.spotify.com/artist/36QJpDe2go2KgaRleHCDTp'
# album_url =''
# track_url = ''

#認証パート
#client ID
# my_id = 'da5b39a37d8d422e9f22d5c05a7a56e6' 
#client secret
# my_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
# ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
# spotify = spotipy.Spotify(client_credentials_manager = ccm)

# results = spotify.artist_related_artists(artist_url)
# result = results['artists']
# related_df = pd.DataFrame(index=[], columns=['Name', 'Genres', 'Images_url', 'Popularity', 'URL', 'URI'])
#resuktの数をカウントしてfor文を回す
# for i in range(len(result)): 
#     related_df= related_df.append({
#         'Name' : result[i]['name'],
#         'Genres' : result[i]['genres'],
#         'Images_url' : result[i]['images'][0]['url'],
#         'Popularity' : result[i]['popularity'],
#         'URL' : result[i]['external_urls']['spotify'], 
#         'URI' : result[i]['uri']}, ignore_index=True)
# print(related_df)
# def index(request):
#     return render(request,"mypage/index.html")

# import sys
# import pprint
# import spotipy
# from django.shortcuts import render
# from spotipy.oauth2 import SpotifyClientCredentials


# Oath2
# client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6'
# client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
# -*- coding: utf-8 -*-

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret,language='ja'))
# 検索
# search_str = sys.argv[1]

# results = sp.search(q=search_str, limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(f"{idx:03d}\t{track['name']}\t")

# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6'
# client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'


# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# keyword = '115万キロのフィルム'
# keyword = searchForm.cleaned_data['keyword'] 

# results = sp.search(q=keyword, limit=10, market="JP")
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx + 1, track['name'])


# -*- coding: utf-8 -*-
# import sys
# import pprint
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from .forms import SearchForm 


# # Oath2
# client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6'
# client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# keyword = '115万キロのフィルム'
# keyword = searchForm.cleaned_data['keyword'] 

# results = sp.search(q=keyword, limit=10, market="JP")
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx + 1, track['name'])

# Create your views here.
# def index(request):
#     searchForm = SearchForm(request.GET)
    # searchForm変数に正常なデータがあれば
    # if searchForm.is_valid():
    #     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret, language='ja'))
        # 検索
        # search_str = sys.argv[1]

        # results = sp.search(q=search_str, limit=20)
        #     for idx, track in enumerate(results['tracks']['items']):
        # print(f"{idx:03d}\t{track['name']}\t")

        # return render(request,"mypage/index.html")
