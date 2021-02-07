from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Department(models.TextChoices):
        department_01 = '01', 'Department 01: Novos Biopesticidas'
        department_02 = '02', 'Department 02: Proteção de Culturas Específicas'
        department_03 = '03', 'Department 03: Gestão de Dados e Análise de Risco'
        department_04 = '04', 'Department 04: Monitorização e Diagnóstico'
        department_05 = '05', 'Department 05: Novas Formulações e Matrizes para a Aplicação de Biopesticidas'
        department_06 = '06', 'Department 06: Gestão'

class Report(models.Model):
    name = models.CharField(max_length=200)
#   user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Name:')
    depto = models.CharField(
        max_length=100, verbose_name='Department:',
        choices= Department.choices,
        default= Department.department_01
    )
    date = models.DateField(verbose_name='Week Starts on:')
    description = models.TextField(blank=False, null=False, verbose_name= 'Description:')

    def __str__(self):
        return self.user
