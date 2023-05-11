from django.shortcuts import render, get_object_or_404,HttpResponse
from football.models import Scores, Players, Player_matches

# Create your views here.  

def index(request):
    return render(request, 'football/html/index.html', { 'data' : Scores.objects.all().order_by('-match_date') })

def players(request):
    return render(request, 'football/html/players.html',{ 'data' : Players.objects.all()})

def champions_league_2023(request):
    return render(request, 'football/html/champions_league.html',{ 'data' : Players.objects.all()})

def show_player(request,players_id):
    post = get_object_or_404(Players, pk=players_id)
    matches = Player_matches.objects.filter(player=players_id).order_by('-match_date')

    context = {
        'post':post,
        'matches':matches,
        'active':str(post.pk)
        }

    return render(request,'football/html/players_post.html',context=context)