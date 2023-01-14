from django.shortcuts import render
from app.models import Profession_statistic, SalaryByCity, PercentageByCity, TopSkills2015, TopSkills2016, TopSkills2017, TopSkills2018, \
    TopSkills2019, TopSkills2020, TopSkills2021, TopSkills2022
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
    skills2015 = TopSkills2015.objects.all()
    skills2016 = TopSkills2016.objects.all()
    skills2017 = TopSkills2017.objects.all()
    skills2018 = TopSkills2018.objects.all()
    skills2019 = TopSkills2019.objects.all()
    skills2020 = TopSkills2020.objects.all()
    skills2021 = TopSkills2021.objects.all()
    skills2022 = TopSkills2022.objects.all()
    response_data = {
        "skills2015": skills2015,
        "skills2016": skills2016,
        "skills2017": skills2017,
        "skills2018": skills2018,
        "skills2019": skills2019,
        "skills2020": skills2020,
        "skills2021": skills2021,
        "skills2022": skills2022,
    }
    return render(request, "skills.html", response_data)

def lastvacancies(request):
    return render(request, 'lastvacancies.html')