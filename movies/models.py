from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    def __str__(self):
        return self.title