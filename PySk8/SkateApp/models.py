from django.contrib.auth.models import User
from django.db import models

RATING = (
    (1, "1.0"),
    (2, "2.0"),
    (3, "3.0"),
    (4, "4.0"),
    (5, "5.0"),
)


class Image(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(choices=RATING)
    description = models.TextField()
    image = models.ImageField(upload_to='Images')
    owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    avatar = models.ImageField(upload_to='avatar_image', blank=True, null=True)
    warn = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
