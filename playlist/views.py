from django.shortcuts import render
from mypage.models import playlists,musics
# Create your views here.

def index(request):
    if request.POST:
        new_playlist = playlists()
        new_playlist.name = request.POST.get('playlist_name')
        new_playlist.save()
        for music_id in request.POST.get('music_id'):
            music = musics()
    # プレイリスト一覧を取ってくる
    all_playlist = playlists.objects.all()

    return render(request,"playlist/index.html", context={"all_playlist":all_playlist})