from django.shortcuts import render
from http import client
from django.shortcuts import render
from steam.client import SteamClient
from dota2.client import Dota2Client
from rest_framework import viewsets
from dotaApi.models import *
from dotaApi.serializers import *

from django.http import HttpResponse

# class PlayerContentViewSet(viewsets.ModelViewSet):
#     queryset = Player.objects.all()
#     search_fields = ['name','matches','rank']
#     serializer_class = PlayerSerializer


# class MatchesContentViewSet(viewsets.ModelViewSet):
#     queryset = Match.objects.all()
#     search_fields = [ 'match_id', 'result', 'game_mode', 'duration', 'kills', 'deaths', 'assists']
#     serializer_class = MatchSerializer

client = SteamClient()
dota = Dota2Client(client)

class PlayerView():
    def player_profile_view(request):
        return dota.request_profile('1054212342')

    def player_card_view(request):
        return dota.request_profile_card('1054212342')

    def profile_stats_view(request):
        return dota.request_profile_stats('1054212342')

    def player_stats_view(request):
        return dota.request_player_stats('1054212342')
    
    def match_details(request):
        return dota.request_match_details('6718366200')

    def save_player_data(self, request):
        if request.method == "POST":
            player = Player()
            player.name = PlayerView.player_profile_view()
            player.matches = PlayerView.player_stats()
            player.rank = PlayerView.player_card_view()
            player.save()
        return HttpResponse('Данные отправлены в модель')
            

    # def player_info():