from django.contrib import admin
from app.models import Profession_statistic
from app.models import SalaryByCity, PercentageByCity, TopSkills2015, TopSkills2016, TopSkills2017, TopSkills2018, \
    TopSkills2019, TopSkills2020, TopSkills2021, TopSkills2022

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class Profession_statisticResource(resources.ModelResource):
    class Meta:
        model = Profession_statistic

class Profession_statisticAdmin(ImportExportActionModelAdmin):
    resource_class = Profession_statisticResource
    list_display = [field.name for field in Profession_statistic._meta.fields if field.name != 'id']

admin.site.register(Profession_statistic, Profession_statisticAdmin)



class SalaryByCityResource(resources.ModelResource):
    class Meta:
        model = SalaryByCity

class StatisticByYearAdmin(ImportExportActionModelAdmin):
    resource_class = SalaryByCityResource
    list_display = [field.name for field in SalaryByCity._meta.fields if field.name != 'id']

admin.site.register(SalaryByCity, StatisticByYearAdmin)


class PercentageByCityResource(resources.ModelResource):
    class Meta:
        model = PercentageByCity

class PercentageByCityAdmin(ImportExportActionModelAdmin):
    resource_class = PercentageByCityResource
    list_display = [field.name for field in PercentageByCity._meta.fields if field.name != 'id']

admin.site.register(PercentageByCity, PercentageByCityAdmin)



class TopSkills2015Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2015


class TopSkills2015Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2015Resource
    list_display = [field.name for field in TopSkills2015._meta.fields if field.name != 'id']


admin.site.register(TopSkills2015, TopSkills2015Admin)


class TopSkills2016Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2016


class TopSkills2016Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2016Resource
    list_display = [field.name for field in TopSkills2016._meta.fields if field.name != 'id']


admin.site.register(TopSkills2016, TopSkills2016Admin)


class TopSkills2017Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2017


class TopSkills2017Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2017Resource
    list_display = [field.name for field in TopSkills2017._meta.fields if field.name != 'id']


admin.site.register(TopSkills2017, TopSkills2017Admin)


class TopSkills2018Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2018


class TopSkills2018Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2018Resource
    list_display = [field.name for field in TopSkills2018._meta.fields if field.name != 'id']


admin.site.register(TopSkills2018, TopSkills2018Admin)


class TopSkills2019Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2019


class TopSkills2019Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2019Resource
    list_display = [field.name for field in TopSkills2019._meta.fields if field.name != 'id']


admin.site.register(TopSkills2019, TopSkills2019Admin)


class TopSkills2020Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2020


class TopSkills2020Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2020Resource
    list_display = [field.name for field in TopSkills2020._meta.fields if field.name != 'id']


admin.site.register(TopSkills2020, TopSkills2020Admin)


class TopSkills2021Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2021


class TopSkills2021Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2021Resource
    list_display = [field.name for field in TopSkills2021._meta.fields if field.name != 'id']


admin.site.register(TopSkills2021, TopSkills2021Admin)


class TopSkills2022Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2022


class TopSkills2022Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2022Resource
    list_display = [field.name for field in TopSkills2022._meta.fields if field.name != 'id']


admin.site.register(TopSkills2022, TopSkills2022Admin)

