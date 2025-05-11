from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    imdb = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.CharField(max_length=4)
    sposter = models.ImageField(upload_to='media_posters/')
    bposter = models.ImageField(upload_to='media_posters/')
    description = models.TextField()
    genre = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    url = models.URLField()
    trailer = models.FileField(upload_to='media_trailers/')
    medium = models.FileField(upload_to='media_files/')
