from django.db import models


# artist名
# 動画キー
# イベントキー

class Artist(models.Model):
    name = models.CharField("aritst名",max_length=128)
    youtube = models.CharField("動画",max_length=128)
    live = models.CharField("ライブ",max_length=128)



