from django.contrib import admin
from app.models import Profession_statistic
from app.models import SalaryByCity, PercentageByCity

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
