from dotaApi.models import Player, Match
from rest_framework import serializers

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Player
        fields = [
            'name',
            'matches',
            'rank'
        ]

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Match
        fields = [ 
            'match_id', 
            'result', 
            'game_mode', 
            'duration', 
            'kills', 
            'deaths', 
            'assists'
        ]
           
        