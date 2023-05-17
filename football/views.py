from django.shortcuts import render, get_object_or_404,HttpResponse
from django.db.models import Q
from football.models import Scores, Players, Player_matches,Champions_League_Scores

# Create your views here.  

def index(request):
    return render(request, 'football/html/index.html', { 'data' : Scores.objects.all().order_by('-match_date') })

def players(request):
    return render(request, 'football/html/players.html',{ 'data' : Players.objects.all()})

def teams(request):
    return render(request, 'football/html/teams.html',)

def manchester_city(request):
    return render(request, 'football/html/manchester_city.html',{ 'matches' : Scores.objects.filter(Q(first_team='Man City') | Q(second_team='Man City'))})

def real_madrid(request):
    return render(request, 'football/html/real_madrid.html',{ 'matches' : Scores.objects.filter(Q(first_team='Real Madrid') | Q(second_team='Real Madrid'))})

def champions_league_2023(request):
    return render(request, 'football/html/champions_league.html',{ 'data' : Champions_League_Scores.objects.all().order_by('-match_date')})

def show_player(request,players_id):
    post = get_object_or_404(Players, pk=players_id)
    matches = Player_matches.objects.filter(player=players_id).order_by('-match_date')

    context = {
        'post':post,
        'matches':matches,
        'active':str(post.pk)
        }

    return render(request,'football/html/players_post.html',context=context)