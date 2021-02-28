from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    founded = models.IntegerField()


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    jersey_number = models.IntegerField()
