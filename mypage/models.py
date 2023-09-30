from django.db import models
from django.utils import timezone
# from django.contrib.postgres.fields import JSONField
# Create your models here.

# spotify_genre
# class spotify_genre(models.Model):
#     spotify_genre_id = models.AutoField(primary_key = True) 
#     name = models.CharField('ジャンル',max_length=100)
#     genre = models.ManyToManyField("type")

class spotify_genre(models.Model):
    spotify_genre_id = models.AutoField(primary_key = True) 
    name = models.CharField('ジャンル',max_length=100)
    # type = models.ManyToManyField("genre")

# genre
# class type(models.Model):
#     type_id = models.AutoField(primary_key = True) 
#     name = models.CharField('ジャンル',max_length=100)
#     spotify_type = models.ManyToManyField("spotify_genre")
class genre(models.Model):
    genre_id = models.AutoField(primary_key = True) 
    name = models.CharField('ジャンル',max_length=100)
    spotify_type = models.ManyToManyField("spotify_genre")

# 検索結果_検索キーワード
class search_results(models.Model):
    search_results_id = models.AutoField(primary_key = True) 
    contents = models.JSONField(blank=True, null=True)
    keyword = models.CharField('キーワード',max_length=1000)
    genre_id = models.ForeignKey(genre,on_delete=models.CASCADE,default=1)
    page_num = models.IntegerField()
    musics_id = models.CharField('楽曲名', max_length=100)
    artists_id = models.CharField('アーティスト名', max_length=100)
    # auto_now_add はインスタンスの作成(DBにINSERT)する度に更新
    # created_at = models.DateTimeField('作成日時',auto_now_add=True,default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
    # updated_at = models.DateTimeField('更新日時',auto_now=True,default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.keyword

# genre to spotify
# class genre_spotify(models.Model):
#     genre_id = models.ManyToManyField(genre)
#     spotify_genre_id = models.ManyToManyField(spotify_genre)


# users
class users(models.Model):
    users_id = models.AutoField(primary_key = True) 
    name = models.CharField('ユーザ名',max_length=100)
    spotify_account = models.CharField('ユーザアカウント',max_length=100)

# aritsts
class artists(models.Model):
    artist_uuid = models.CharField('Aritist_UUID',max_length=100,default="")
    aritsts_id = models.AutoField(primary_key = True)
    name = models.CharField('アーティスト名',max_length=100)
    aritsts_images = models.URLField()
    aritsts_uri = models.URLField()


# musics
class musics(models.Model):
    musics_id = models.AutoField(primary_key = True)
    name = models.CharField('音楽名',max_length=100)
    aritist_id = models.ForeignKey(artists,on_delete=models.CASCADE)
    spotify_uuid = models.CharField(max_length=100)
    musics_images = models.URLField(default="")
    musics_uri = models.URLField(default="")

# playlist
class playlists(models.Model):
    playlists_id = models.ForeignKey(users,on_delete=models.CASCADE)
    name = models.CharField('プレイリストネーム',max_length=100)
    user_id = models.IntegerField()
    Public = models.BooleanField(default=True)
    description = models.TextField()
    # auto_now_add はインスタンスの作成(DBにINSERT)する度に更新
    created_at = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField('作成日時',auto_now_add=True,default=timezone.now)
    # auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
    # updated_at = models.DateTimeField('更新日時',auto_now=True,default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    music = models.ManyToManyField(to=musics)


# musics_in_playlist
class musics_in_playlist(models.Model):
    musics_in_playlist_id = models.AutoField(primary_key = True)
    playlists_id = models.ManyToManyField(playlists)
    musics_id = models.ManyToManyField(musics)



# 検索結果_中間
# class result_middle(models.Model):
#     music_id = models.CharField('楽曲名', max_length=100)
#     keyword_id = models.CharField('キーワード', max_length=100)

#     def __str__(self):
#         return self.music_id

#     # title = models.CharField('楽曲名', max_length=100)
#     # album = models.URLField(blank=True)
#     # artist = models.URLField(blank=True)
#     # artist_name = models.CharField('Artist名', max_length=100)
#     # preview = models.URLField(blank=True)
    
# # 検索結果_詳細
# class resule_detail(models.Model):
#     music_id = models.CharField('楽曲名', max_length=100)
#     title = models.CharField('タイトル', max_length=100)
#     album_images = models.URLField(blank=False)
#     artist_images = models.URLField(blank=False)
#     artist = models.CharField('アーティスト名', max_length=50)
#     previews = models.URLField(blank=False)
#     created_at = models.DateTimeField('作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField('更新日時', auto_now=True)

# # プレイリスト_アイテム
# class playlist_item(models.Model):
#     music_uri = models.URLField(blank=False)
#     music_id = models.CharField('楽曲名', max_length=100)
#     artist = models.CharField('アーティスト名', max_length=50)
#     playlist_id = models.IntegerField(blank=True, null=True)

# # プレイリスト中間

# # class playlist_middle(models.Model):
# #     playlist_id = models.IntegerField(blank=True, null=True)
# #     id = models.IntegerField(blank=True, null=True)
# #     created_at = models.DateTimeField('作成日時', auto_now_add=True)
# #     updated_at = models.DateTimeField('更新日時', auto_now=True)

# class playlist_total(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     name = models.CharField('プレイリストネーム', max_length=100)

# # プレイリスト
# class Main(models.Model):
#     # id = models.AutoField(primary_key=True)
#     # Janru = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     genru = models.CharField('ジャンル', max_length=50)
#     keyword = models.CharField('キーワード', max_length=100)
#     music = models.CharField('楽曲名', max_length=100)
#     artist = models.CharField('アーティスト名', max_length=50)
#     al_images = models.URLField(blank=False)
#     page_num = models.PositiveSmallIntegerField('ページ数', blank=True, default=0)
#     popularity = models.PositiveSmallIntegerField('人気順', blank=True, default=0)
#     rank = models.PositiveSmallIntegerField('順位', blank=True, default=0)
#     created_at = models.DateTimeField('作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField('更新日時', auto_now=True)

#     def __str__(self):
#         return self.artist

# class Artist(models.Model):
#     ar_images = models.URLField(blank=False)
#     aritist_key = models.CharField('アーティスト',max_length=100)

#     def __str__(self):
#         return self.aritist_key

# class Janru_search(models.Model):
#     janru_name = models.CharField('ジャンル名',max_length=50)

#     def __str__(self):
#         return self.janru_name


# class Janru_middle(models.Model):
#     janru_name = models.CharField('ジャンル名',max_length=50)
    
#     def __str__(self):
#         return self.janru_name

# class Janru_spotify(models.Model):
#     janru_name = models.CharField('ジャンル名',max_length=50)
#     janru_ID = models.PositiveSmallIntegerField('ジャンルID', blank=True, default=0)

#     def __str__(self):
#         return self.janru_name
