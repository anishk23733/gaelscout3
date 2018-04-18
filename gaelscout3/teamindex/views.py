from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from teamindex.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

# Create your views here.
def home(request):
    return render(request, 'index.html')

def teamindex(request):
    teams = Teams.objects.all()
    paginator = Paginator(teams, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    teams = paginator.get_page(page)
    return render(request, 'teamindex.html', {'teams': teams})

def dashboard(request, team_number):
    team = Teams.objects.get(name=team_number)
    return render(request, 'dashboard.html', {'team':team})

def divisionindex(request):
    teams = ResearchTeams.objects.all()
    return render(request, 'divisionindex.html', {'teams': teams})