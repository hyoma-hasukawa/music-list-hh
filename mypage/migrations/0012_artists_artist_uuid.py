# Generated by Django 4.1.2 on 2023-09-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0011_alter_playlists_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='artist_uuid',
            field=models.CharField(default='', max_length=100, verbose_name='Aritist_UUID'),
        ),
    ]
