# from django.shortcuts import render
# import spotipy

# # Create your views here.
# def index(request):
#     return render(request,"mypage/index.html")

# -*- coding: utf-8 -*-
import sys
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Oath2
client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6'
client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret, language='ja'))
# 検索
search_str = sys.argv[1]

results = sp.search(q=search_str, limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(f"{idx:03d}\t{track['name']}\t")