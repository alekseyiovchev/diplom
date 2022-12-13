from django.shortcuts import render
from football.models import Scores,Players

# Create your views here.

def index(request):
    return render(request, 'football/html/index.html', { 'data' : Scores.objects.all().order_by('-match_date') })

def players(request):
    return render(request, 'football/html/players.html',{ 'data' : Players.objects.all()})