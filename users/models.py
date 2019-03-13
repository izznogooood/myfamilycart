from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')
    name = models.CharField(max_length=200)
    count = models.PositiveIntegerField()

    class Meta:
        ordering = ["-count"]

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.email}, {self.user.username}'




