from django.db import models

# Create your models here.
class Main(models.Model):
    # id = models.AutoField(primary_key=True)
    # Janru = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genru = models.CharField('ジャンル', max_length=50)
    keyword = models.CharField('キーワード', max_length=100)
    music = models.CharField('楽曲名', max_length=100)
    artist = models.CharField('アーティスト名', max_length=50)
    al_images = models.URLField(blank=False)
    page_num = models.PositiveSmallIntegerField('ページ数', blank=True, default=0)
    popularity = models.PositiveSmallIntegerField('人気順', blank=True, default=0)
    rank = models.PositiveSmallIntegerField('順位', blank=True, default=0)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.artist
    
class result(models.Model):
    title = models.CharField('楽曲名', max_length=100)
    album = models.URLField(blank=True)
    artist = models.URLField(blank=True)
    artist_name = models.CharField('Artist名', max_length=100)
    preview = models.URLField(blank=True)

class Artist(models.Model):
    ar_images = models.URLField(blank=False)
    aritist_key = models.CharField('アーティスト',max_length=100)

    def __str__(self):
        return self.aritist_key

class Janru_search(models.Model):
    janru_name = models.CharField('ジャンル名',max_length=50)

    def __str__(self):
        return self.janru_name


class Janru_middle(models.Model):
    janru_name = models.CharField('ジャンル名',max_length=50)
    
    def __str__(self):
        return self.janru_name

class Janru_spotify(models.Model):
    janru_name = models.CharField('ジャンル名',max_length=50)
    janru_ID = models.PositiveSmallIntegerField('ジャンルID', blank=True, default=0)

    def __str__(self):
        return self.janru_name
