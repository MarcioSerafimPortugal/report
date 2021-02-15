from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Department(models.TextChoices):
        department_01 = 'Department 01: Novos Biopesticidas'
        department_02 = 'Department 02: Proteção de Culturas Específicas'
        department_03 = 'Department 03: Gestão de Dados e Análise de Risco'
        department_04 = 'Department 04: Monitorização e Diagnóstico'
        department_05 = 'Department 05: Novas Formulações e Matrizes para a Aplicação de Biopesticida'
        department_06 = 'Department 06: Gestão'


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    depto = models.CharField(
        max_length=100, verbose_name='Department:',
        choices= Department.choices,
        default= Department.department_01
    )
    date = models.DateField(verbose_name='Week Starts on:')
    description = models.TextField(blank=False, null=False, verbose_name= 'Description:')


class Department4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(verbose_name='Week Starts on:')
    research_activities = models.TextField(blank=False, null=False, verbose_name= 'Research Activities:')
    internal_meetings = models.TextField(blank=False, null=False, verbose_name= 'Internal Meetings:')
    external_meetings = models.TextField(blank=False, null=False, verbose_name= 'External Meetings and Stakeholders Engagement:')
    service_tools = models.TextField(blank=False, null=False, verbose_name= 'Service / Tools Development:')
    grant = models.TextField(blank=False, null=False, verbose_name= 'Grant / Calls Preparation:')
    training= models.TextField(blank=False, null=False, verbose_name= 'Training / Webnars Attendance:')

