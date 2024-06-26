# Generated by Django 4.1.2 on 2023-07-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0009_alter_musics_spotify_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musics_in_playlist',
            name='musics_images',
        ),
        migrations.RemoveField(
            model_name='musics_in_playlist',
            name='musics_uri',
        ),
        migrations.AddField(
            model_name='musics',
            name='musics_images',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='musics',
            name='musics_uri',
            field=models.URLField(default=''),
        ),
    ]
