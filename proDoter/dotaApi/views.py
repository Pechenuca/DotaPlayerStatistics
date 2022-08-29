from http import client
from re import template
from steam.client import SteamClient
from dota2.client import Dota2Client
from dotaApi.models import *
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

client = SteamClient()
dota = Dota2Client(client)

@csrf_exempt
def index(request):
    template = loader.get_template('dotaApi/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
# 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

class PlayerView(View):
    model = Player
    def set_api_data(request):
        api_data = request.POST.get('api_data')
        template = loader.get_template('dotaApi/setter.html')
        Player.objects.create(name = api_data)
        context = {
            'data' : dota.request_profile(1054212342)
        }
        return HttpResponse(template.render(context, request))

    # def save_player_data(self, request):
    #     if request.method == "POST":
    #         player = Player()
    #         player.name = PlayerView.player_profile_view()
    #         # player.matches = PlayerView.player_stats()
    #         # player.rank = PlayerView.player_card_view()
    #         player.save()
    #     return HttpResponse('Данные отправлены в модель')
            
