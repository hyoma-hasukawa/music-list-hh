# Generated by Django 4.1.2 on 2023-04-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='janru',
            new_name='genru',
        ),
    ]
