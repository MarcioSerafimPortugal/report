from django.db import models

#Create your models here.
class Department(models.TextChoices):
        department_01 = 'Department 01: Novos Biopesticidas'
        department_02 = 'Department 02: Proteção de Culturas Específicas'
        department_03 = 'Department 03: Gestão de Dados e Análise de Risco'
        department_04 = 'Department 04: Monitorização e Diagnóstico'
        department_05 = 'Department 05: Novas Formulações e Matrizes para a Aplicação de Biopesticida'
        department_06 = 'Department 06: Gestão'



class Report(models.Model):
    name = models.CharField(max_length=200)
    depto = models.CharField(
        max_length=100, verbose_name='Department:',
        choices= Department.choices,
        default= Department.department_01
    )
    date = models.DateField(verbose_name='Week Starts on:')
    description = models.TextField(blank=False, null=False, verbose_name= 'Description:')

    def __str__(self):
        return self.name

class Department4(models.Model):
    name = models.CharField(max_length=200, verbose_name= 'Name:')
    date = models.DateField(verbose_name='Week Starts on:')
    research_activities = models.TextField(blank=False, null=False, verbose_name= 'Research Activities:')
    internal_meetings = models.TextField(blank=False, null=False, verbose_name= 'Internal Meetings:')
    external_meetings = models.TextField(blank=False, null=False, verbose_name= 'External Meetings and Stakeholders Engagement:')
    service_tools = models.TextField(blank=False, null=False, verbose_name= 'Service / Tools Development:')
    grant = models.TextField(blank=False, null=False, verbose_name= 'Grant / Calls Preparation:')
    training= models.TextField(blank=False, null=False, verbose_name= 'Training / Webnars Attendance:')

    def __str__(self):
        return self.name
