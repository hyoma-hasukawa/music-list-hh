from django.db import models


# artist名
# 動画キー
# イベントキー

class Artist(models.Model):
    id = models.BigAutoField("id", primary_key=True)
    name = models.CharField("aritst名", max_length=128)
    youtube = models.CharField("動画", max_length=128)
    live = models.CharField("ライブ", max_length=128)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)



