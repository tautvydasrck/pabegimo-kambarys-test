from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from pytz import utc

from .models import Client, GameType, Game

def index(request):
    games_list = Game.objects.order_by('date_time')
    games_list_upcoming = []
    games_list_history = []
    for game in games_list:
        if game.date_time > datetime.now(utc):
            games_list_upcoming.append(game)
        else:
            games_list_history.append(game)
    games_list_history = games_list_history[::-1]
    context = {
        'games_list_upcoming': games_list_upcoming,
        'games_list_history': games_list_history
        }
    return render(request, 'game_registration/index.html', context)

def edit_game(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Tokio žaidimo nėra")
    game_types_list = GameType.objects
    return render(request, 'game_registration/edit_game.html', {'game': game, 'game_types_list': game_types_list})

def game_types(request):
    game_types_list = GameType.objects
    context = {'game_types_list': game_types_list}
    return render(request, 'game_registration/game_types.html', context)

def edit_game_submit(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.date_time = request.POST['inputDateTime']
    game.game_type_id = request.POST['selectGameType']
    client = Client.objects.get(pk=game.client_id)
    client.name = request.POST['inputClient']
    client.email = request.POST['inputEmail']
    client.phone = request.POST['inputPhone']
    client.juridical = request.POST.get('checkJuridical', 0)
    game.hall = request.POST.get('checkHall', 0)
    game.price = request.POST['inputPrice']
    game.save()
    client.save()
    return HttpResponseRedirect(reverse('game_registration:index'))

def delete_game(request, game_id):
    if request.method == 'POST':
        Game.objects.filter(id=game_id).delete()
    return HttpResponseRedirect(reverse('game_registration:index'))

def new_game(request):
    game_types_list = GameType.objects
    context = {'game_types_list': game_types_list}
    return render(request, 'game_registration/new_game.html', context)

def new_game_submit(request):
    new_client = Client(
        name = request.POST['inputClient'],
        email = request.POST['inputEmail'],
        phone = request.POST['inputPhone'],
        juridical = request.POST.get('checkJuridical', 0)
    )
    new_client.save()
    new_game = Game(
        date_time = request.POST['inputDateTime'],
        game_type_id = request.POST['selectGameType'],
        client_id = new_client.id,
        hall = request.POST.get('checkHall', 0),
        price = request.POST['inputPrice']
    )
    new_game.save()
    return HttpResponseRedirect(reverse('game_registration:index'))

def game_types_edit(request, game_type_id):
    game_type = get_object_or_404(GameType, pk=game_type_id)
    game_type.name = request.POST['inputName']
    game_type.price = request.POST['inputPrice']
    game_type.save()
    return HttpResponseRedirect(reverse('game_registration:game_types'))

def game_types_new_submit(request):
    new_game_type = GameType(
        name = request.POST['inputName'],
        price = request.POST['inputPrice']
    )
    new_game_type.save()
    return HttpResponseRedirect(reverse('game_registration:game_types'))

def game_types_delete(request, game_type_id):
    if request.method == 'POST':
        GameType.objects.filter(id=game_type_id).delete()
    return HttpResponseRedirect(reverse('game_registration:game_types'))
