from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Song(models.Model):
    title = models.CharField(max_length=20)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.CharField(max_length=20000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

