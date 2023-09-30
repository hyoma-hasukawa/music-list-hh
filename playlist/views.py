from django.shortcuts import render
from mypage.models import playlists,musics,users
# Create your views here.
from pprint import pprint 
# ログイン
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.POST:
        new_playlist = playlists()
        new_playlist.name = request.POST.get('playlist_name')
        pprint("aaaaaa")
        pprint(request.user)
        new_playlist.user_id = request.user.id
        #user_id 
        # new_playlist.playlists_id = request.user
        # new_playlist.playlists_id_id = request.user.id
        new_playlist.playlists_id_id = request.user
        new_playlist.description = "aaa"
        if request.user.is_authenticated:
            new_playlist.playlists_id = users.objects.filter(users_id=request.user.id).first()
        # else:
        #     new_playlist.playlists_id = users()
        new_playlist.save()
        for music_id in request.POST.getlist('music_id'):
            music = musics()
    # プレイリスト一覧を取ってくる user_id指定
    all_playlist = playlists.objects.filter(user_id=request.user.id)
    # all_playlist = playlists.objects.all()

    return render(request,"playlist/index.html", context={"all_playlist":all_playlist})