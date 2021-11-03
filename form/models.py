from django.db import models


class Anamnese(models.Model):
    pregnant = models.BooleanField('Gestante?', blank=True, default=False)
    bleeding = models.BooleanField('Hemorragia?', blank=True, default=False)
    pressure = models.BooleanField('Pressão?', blank=True, default=False)
    allergy = models.BooleanField('Alergia?', blank=True, default=False)
    systemic_disease = models.CharField('Doença Sistêmica?', max_length=300, blank=True)
    medicine = models.CharField('Medicamentos?', max_length=300, blank=True)

class Tooth(models.Model):
    number = models.IntegerField('Número do dente', blank=True)
    report = models.CharField('Relatório', max_length=300, blank=True)

    anamnese = models.ForeignKey(Anamnese, on_delete=models.CASCADE, related_name='dente')
