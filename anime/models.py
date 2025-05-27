from django.db import models
from users.models import CustomUser
from django.db import models

class Anime(models.Model):
    anilist_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    episodes = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    members = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='user_ratings')
    rating = models.FloatField()

    def __str__(self):
        return f"{self.user.username} rated {self.anime.name} - {self.rating}"
