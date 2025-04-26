from django.db import models
from artists.models import Artist
from genres.models import Genre


class Song(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='songs')
    release_date = models.DateField(null=True, blank=True)
    artists = models.ManyToManyField(Artist, related_name='songs')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
