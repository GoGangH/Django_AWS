# Generated by Django 4.0 on 2022-11-06 14:35

from docker_server.django import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_demo', '0003_playlist_cover_img_song_album_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='tags',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='moodtag',
            name='tag_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='playlisttag',
            name='tag_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='situationtag',
            name='tag_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topictag',
            name='tag_name',
            field=models.CharField(max_length=100),
        ),
    ]
