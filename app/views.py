from django.shortcuts import render
from app.models import Profession_statistic


# Create your views here.
def index(request):
    return render(request, 'index.html')

def demand(request):
    return render(request, 'demand.html')

def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

def lastvacancies(request):
    return render(request, 'lastvacancies.html')