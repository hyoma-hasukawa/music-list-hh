from django.shortcuts import render
from mypage.models import playlists,musics
# Create your views here.

def index(request):
    if request.POST:
        new_playlist = playlists()
        new_playlist.name = request.POST.get('playlist_name')
        new_playlist.user_id = 1
        #user_id 
        # new_playlist.playlists_id = request.user
        # new_playlist.playlists_id_id = request.user.id
        new_playlist.playlists_id_id = 1
        new_playlist.save()
        for music_id in request.POST.getlist('music_id'):
            music = musics()
    # プレイリスト一覧を取ってくる
    all_playlist = playlists.objects.all()

    return render(request,"playlist/index.html", context={"all_playlist":all_playlist})