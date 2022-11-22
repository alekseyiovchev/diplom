from django.shortcuts import render
from football.models import Scores

# Create your views here.

def index(request):
    return render(request, 'football/html/index.html', { 'data' : Scores.objects.all().order_by('-match_date') })