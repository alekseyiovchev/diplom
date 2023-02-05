from django.shortcuts import render, get_object_or_404,HttpResponse
from football.models import Scores, Players

# Create your views here.  

def index(request):
    return render(request, 'football/html/index.html', { 'data' : Scores.objects.all().order_by('-match_date') })

def players(request):
    return render(request, 'football/html/players.html',{ 'data' : Players.objects.all()})

def show_player(request,players_id):
    return HttpResponse(players_id)
    # post = get_object_or_404(Players, pk=players_id)

    # return render(request,'football/html/players_post.html',context=post.name )