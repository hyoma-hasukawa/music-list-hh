# -*- coding: utf-8 -*-
import math
import spotipy
# datetimeモジュールを使った現在の日付と時刻の取得
import datetime
# Json 
import json
import pprint
# 関数がimportされていなかった
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mypage.models import playlists, search_results,genre,spotify_genre,musics,artists


# inputから検索結果を持ってくる
def index(request):
    query = request.POST.get('search')
    page_num = request.POST.get('page_num') or "1"
    # 現在のページ数が入る (例　p5 → int 4)
    page_num = int(page_num)
    # play_count = request.POST.getlist('play_count[]')
    song_id = request.POST.get('song_id')
    #　人気の楽曲ランキングを取得
    populary = request.POST.get('populary')
    # 有効・無効
    valid = request.POST.get('str')
    # 無効
    # invalid = request.POST.get('flexRadioDefault')
    genre_name = request.POST.get('genre')
    # query（入力内容）をspotifyに検索する
    client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6' 
    client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    #
    genres = sp.recommendation_genre_seeds()
    pprint.pprint(genres)
    genres = genre.objects.all()
    context = {
        # "genres":genres["genres"]
        "genres":[x.name for x in genres]
        }
    # query（入力内容）が存在する場合
    if query or genre_name:
        keyword = query
        # results = sp.search(q=keyword, market="JP", offset=(page_num - 1) * 10)
        # 201行目の内容を取ってきている
        results = search_others(page_num,keyword,genre_name,sp)
        items=[]
        # 楽曲数
        total=results["tracks"]["total"]
        # 10項目出力するように制限
        limit=results["tracks"]["limit"]
        # 順位
        offset=results["tracks"]["offset"]
        # ページ数計算
        pages=math.ceil(total/limit)
        real_pages = 0
        for page in range(pages):
            # res = sp.search(q=keyword, market="JP", offset=page*10)
            res = search_others(page+1,keyword,genre_name,sp)
            if len(res["tracks"]["items"]) == 0:
                break
            real_pages = page
        # ページのリスト出力
        pages=[x + 1 for x in range(real_pages)]
        # try:
        #     page_count = page_num
        # 渡される値が整数でないとき
        # except PageNotAnInteger:
        #     page_count = page_num(1)
        # 最大ページ数を超えたときには空のページになる
        # except EmptyPage:
        #     page_count = page_num(1)
        for idx, track in enumerate(results['tracks']['items']):
            print(idx + 1, track['name'])
            # items = track['name']
            # results+['tracks']+['items']+数字+['name']
            print(track)
            artist = sp.artist(track['artists'][0]['id'])
            print(artist)
            sec = track["duration_ms"] // 1000
            minites = sec // 60
            sec = sec % 60
            times="{:02}:{:02}".format(minites,sec)

            # 「duration_ms」の分出力
            # minse = (track['duration_ms'] // 1000 )
            # min = int(track['duration_ms'] / 1000 / 60)
            # 「duration_ms」の秒出力
            # sec = int((minse - min)*60)
            # sec_len = len(str(sec))
            #  0埋め
            # if sec_len==1:
            #     sec=sec_int.zfill(1)
            # else:
            #     sec=sec_int
            if len(artist['images']) > 0:
                items.append({"track":track, "artist_image":artist['images'][0]['url'], "times":times})
            else:
                items.append({"track":track, "artist_image":'https://placehold.jp/3d4070/ffffff/150x150.png?text=no%20image', "times":times})
        context.update({
            # 検索した結果を受け取った
            "search_word":keyword,
            # "items":results['tracks']['items']
            "items":items,
            "pagelist":pages,
            "offset":offset,
            # "page_count":page_count,
            "total":total,
            "page_num":page_num,
            # sppotify_genreを送る
            "search_genres": genre.objects.filter(name=genre_name).get().spotify_type.all() if genre.objects.filter(name=genre_name) else list("")
        }) 
        
        return render(request, "mypage/index.html", context)

        # return render(request,"mypage/index.html",context={"search_word":query})
        # for idx, track in enumerate(results['tracks']['items']):
        #     print(idx + 1, track['name'])
        #     print('audio    : ' + track['preview_url'])
        #     print('cover art: ' + track['album']['images'][0]['url'])
        #     print()
            # return render(request,"mypage/index.html")
    elif song_id:
        # query（入力内容）が存在しない場合
        # データを渡さずにレンダリングする。リストとなっている箇所を初期表示するか。ヒットチャートを出力するか。
        # print(idx)
        return render(request, "mypage/index.html", context)
    # 人気順で調べる場合（単体）
    # elif invalid:
    #     # query（入力内容）をspotifyに検索する
    #     client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6' 
    #     client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
    #     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    #     results = sp.search(q=populary, market="JP", offset=(page_num - 1) * 10)
    #     items=[]
    #     # 楽曲数
    #     total=results["tracks"]["total"]
    #     # 10項目出力するように制限
    #     limit=results["tracks"]["limit"]
    #     # 順位
    #     offset=results["tracks"]["offset"]
    #     # ページ数計算
    #     pages=math.ceil(total/limit)
    #     real_pages = 0
    #     for page in range(pages):
    #         res = sp.search(q=populary, market="JP", offset=page*10)
    #         if len(res["tracks"]["items"]) == 0:
    #             break
    #         real_pages = page
    #     # ページのリスト出力
    #     pages=[x + 1 for x in range(real_pages)]
    #     # try:
    #     #     page_count = page_num
    #     # 渡される値が整数でないとき
    #     # except PageNotAnInteger:
    #     #     page_count = page_num(1)
    #     # 最大ページ数を超えたときには空のページになる
    #     # except EmptyPage:
    #     #     page_count = page_num(1)
    #     for idx, track in enumerate(results['tracks']['items']):
    #         print(idx + 1, track['name'])
    #         # items = track['name']
    #         # results+['tracks']+['items']+数字+['name']
    #         print(track)
    #         artist = sp.artist(track['artists'][0]['id'])
    #         print(artist)
    #         # 
    #         sec = track["duration_ms"] // 1000
    #         minites = sec // 60
    #         sec = sec % 60
    #         times="{:02}:{:02}".format(minites,sec)

    #         # 「duration_ms」の分出力
    #         # minse = (track['duration_ms'] // 1000 )
    #         # min = int(track['duration_ms'] / 1000 / 60)
    #         # 「duration_ms」の秒出力
    #         # sec = int((minse - min)*60)
    #         # sec_len = len(str(sec))
    #         #  0埋め
    #         # if sec_len==1:
    #         #     sec=sec_int.zfill(1)
    #         # else:
    #         #     sec=sec_int
    #         if len(artist['images']) > 0:
    #             items.append({"track":track, "artist_image":artist['images'][0]['url'], "times":times})
    #         else:
    #             items.append({"track":track, "artist_image":'https://placehold.jp/3d4070/ffffff/150x150.png?text=no%20image', "times":times})
    #     context = {
    #         # 検索した結果を受け取った
    #         "search_word":query,
    #         # "items":results['tracks']['items']
    #         "items":items,
    #         "pagelist":pages,
    #         "offset":offset,
    #         # "page_count":page_count,
    #         "total":total,
    #         "page_num":page_num
    #     }
        
    #     return render(request, "mypage/index.html")
    else:
        return render(request, "mypage/index.html",context)

# urlに飛ばしているのは「form」・「a」しかない。
def form(request):
    context = request.POST.get('context')
    print(request.POST.get('context'))
    return render(request, 'mypage/index.html',context)

def search_others(page,keyword,genre_name,sp):
    tdy = datetime.date.today()  # 今日の日付の取得
    tdy = tdy + datetime.timedelta(days=5)
    # # ページ・キーワード・ジャンルで検索結果テーブルを検索する
    db_search = search_results.objects.filter(keyword=keyword,genre_id__name=genre_name,page_num=page,updated_at__lte=tdy)
    db_search = db_search.get() if db_search.count() > 0 else None
    # db_search1 = search_results.objects.filter(keyword=keyword,updated_at__lte=tdy)
    results = []
    # データがあったら、それを返す
    if db_search:
        results = json.loads(db_search.contents)
        # return results
    # データが無かったら、
    else:
        if genre_name:
            # spotify_genres = genre.objects.filter(name=genre_name)
            # spotify_genres = spotify_genre.objects.filter(genre__name=genre_name)
            genre_id = genre.objects.filter(name=genre_name).first()
            spotify_genres = genre_id.spotify_type.all()
            # 宿題 : spotify_genresは辞書のリストになっているので、nameをカンマくぎりの文字列にする。
            spotify_genres_k = ",".join([item.name for item in spotify_genres])
            keyword_g = keyword + " genre:" + spotify_genres_k
            if search_results.objects.filter(keyword=keyword,page_num=page,created_at__lte =tdy,genre_id = genre_id):
                results = search_results.objects.filter(keyword=keyword,page_num=page,created_at__lte =tdy,genre_id = genre_id)
                results = json.loads(results.contents)
            else:
                results = sp.search(q=keyword_g, market="JP", offset=(page - 1) * 10)
                # データベースに書き込む
                search_result = search_results(contents = json.dumps(results),keyword = keyword,page_num = page,genre_id = genre_id)
                search_result.save()
        else:
            if search_results.objects.filter(keyword=keyword,page_num=page,created_at__lte =tdy):
                results = search_results.objects.filter(keyword=keyword,page_num=page,created_at__lte =tdy).first()
                results = json.loads(results.contents)
            else:
                results = sp.search(q=keyword, market="JP", offset=(page - 1) * 10)
                # データベースに書き込む
                search_result = search_results(contents = json.dumps(results),keyword = keyword,page_num = page)
                search_result.save()
            # results.save()
    for result in results["tracks"]["items"]:
        artists_sub = sp.artist(result['artists'][0]['id'])
        aritist_image = artists_sub["images"][0]["url"] if len(artists_sub["images"]) > 0 else 'https://placehold.jp/3d4070/ffffff/150x150.png?text=no%20image'
        artist,created = artists.objects.get_or_create(
            artist_uuid = result["artists"][0]["id"],
            name = result["artists"][0]["name"],
            aritsts_images = aritist_image,
            aritsts_uri = result["artists"][0]["uri"]
        )
        music, created = musics.objects.update_or_create(
            name = result["name"],
            spotify_uuid = result["id"],
            musics_images = result["album"]["images"][0]["url"],
            musics_uri = result["preview_url"] if result["preview_url"] else "",
            aritist_id = artist
        )
        # music = musics.objects.filter(spotify_uuid=result.id)
        # if music.length == 0:
        #     music = musics()
        #     music.spotify_uuid = result.id
        #     music.name = result.name
    return results

def playlist(request):
    playlists = request.POST.get('play')
    form = MemberForm()
    return render(request, 'playlist/index.html',context)

# def index(request):
#     jpop = request.POST.get('genre')
#     return render(request, 'mypage/index.html',jpop)

# def paginate_queryset(request):
#     page_num = request.POST.get('page_num') or "0"
#     # 現在のページ数が入る (例　p5 → int 4)
#     page_num = int(page_num)
#     try:
#         pagesa = Paginator.page(page_num)
#     except PageNotAnInteger:
#         pagesa = Paginator.page(1)
#     except EmptyPage:
#         pagesa = Paginator.page(1)
#     return pagesa


# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import sys
# import pprint

# if len(sys.argv) > 1:
#         search_str = sys.argv[1]
# else:
#         search_str = 'Radiohead'

# client_id = 'da5b39a37d8d422e9f22d5c05a7a56e6' 
# client_secret = '1a1ccd9615ce40c0943042e5c8e46f41'
# client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# result = sp.search(q='track:Radiohead', limit=10, offset=0, type='track', market=None) #sp.search(search_str)

# id_list = []
# for track in result['tracks']['items']:
#         id = track['id']
#         id_list.append(id)

# features = sp.audio_features(id_list)
# pprint.pprint(features)
# print(idx)
#         return render(request,"mypage/index.html")


    
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
