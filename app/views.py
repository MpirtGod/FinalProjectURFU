from django.shortcuts import render
from app.models import Profession_statistic
from django.views.generic.list import ListView


# Create your views here.
def index(request):
    return render(request, 'index.html')

def demand(request):
    query_results = Profession_statistic.objects.all()
    return render(request, 'demand.html', {'query_results': query_results})


def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

def lastvacancies(request):
    return render(request, 'lastvacancies.html')