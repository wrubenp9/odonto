from django.db import models
from form.models import Anamnese

# Create your models here.
class Endereco(models.Model):
    estado_choices = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    street = models.CharField(max_length=200, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    complement = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)


class Profile(models.Model):
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Neuma das Opções'),
    )

    full_name = models.CharField('Nome completo', max_length=100, blank=False)
    cpf = models.CharField('CPF', max_length=11)
    rg = models.CharField('RG', max_length=7)
    birth_date = models.DateTimeField('Data de nascimento')

    #RELACIONAMENTOS
    #1 pra 1
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    anamnese = models.OneToOneField(Anamnese, on_delete=models.CASCADE, null=True)