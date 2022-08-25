from dataclasses import fields
from django.db import models
from django import forms


class Match(models.Model):
    match_id = models.IntegerField()
    result = models.CharField(max_length=10)
    game_mode = models.CharField(max_length=10)
    duration = models.DateField(max_length=5)
    # kills = models.IntegerField(max_length=2)
    # deaths = models.IntegerField(max_length=2)
    # assists = models.IntegerField(max_length=2)

    def __str__(self):
        return self.match_id, self.result, self.game_mode, self.duration, self.kills, self.deaths, self.assists

class Player(models.Model):
    name = models.CharField(max_length=100, default=1)
    matches = models.ForeignKey(Match, on_delete=models.CASCADE)
    rank = models.CharField(max_length=10)

    def __str__(self):
        return self.name, self.matches, self.rank
    # def __str__(self):
    #     return self.name
