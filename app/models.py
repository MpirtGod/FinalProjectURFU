from django.db import models
from import_export import resources, fields


# Create your models here.
class Profession_statistic(models.Model):
    year = models.CharField('Год', max_length=4)
    mean_salary = models.CharField('Средняя зарплата', max_length=8)
    profession_mean_salary = models.CharField('Средняя зарплата - Backend-программист', max_length=8)
    vacancy_count = models.CharField('Количество вакансий', max_length=8)
    profession_vacancy_count = models.CharField('Количество вакансий - Backend-программист', max_length=8)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Статистика по профессии'
        verbose_name_plural = 'Статистики по профессии'


class SalaryByCity(models.Model):
    sity = models.CharField('Город', max_length=35)
    salary = models.CharField('Уровень зарплат', max_length=8)

    def __str__(self):
        return str(self.sity)

    class Meta:
        verbose_name = 'Статистика зарплаты по городам'
        verbose_name_plural = 'Статистики зарплат по городам'

class PercentageByCity(models.Model):
    sity = models.CharField('Город', max_length=35)
    percentage = models.CharField('Доля вакансий', max_length=8)

    def __str__(self):
        return str(self.sity)

    class Meta:
        verbose_name = 'Процент вакансий по городам'
        verbose_name_plural = 'Проценты вакансий по городам'

class SkillsByYear(models.Model):
    year = models.CharField('Год', max_length=4)
    top_skills = models.TextField('Навыки')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Топ10 вакансий по году'
        verbose_name_plural = 'Топ10 вакансий по годам'