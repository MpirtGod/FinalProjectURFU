from django.shortcuts import render
from app.models import Profession_statistic, SalaryByCity, PercentageByCity, SkillsByYear
from django.views.generic.list import ListView


# Create your views here.
def index(request):
    return render(request, 'index.html')

def demand(request):
    prof_stat = Profession_statistic.objects.all()
    return render(request, 'demand.html', {'prof_stat': prof_stat})


def geography(request):
    salbycity = SalaryByCity.objects.all()
    perbycity = PercentageByCity.objects.all()
    return render(request, 'geography.html', {'salbycity': salbycity, 'perbycity': perbycity})

def skills(request):
    skillsbyyear = SkillsByYear.objects.all()
    return render(request, 'skills.html', {'skillsbyyear': skillsbyyear})

def lastvacancies(request):
    return render(request, 'lastvacancies.html')