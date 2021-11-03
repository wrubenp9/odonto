# Generated by Django 3.2.8 on 2021-11-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestante', models.BooleanField(blank=True, default=False, verbose_name='Gestante?')),
                ('hemorragia', models.BooleanField(blank=True, default=False, verbose_name='Hemorragia?')),
                ('pressao', models.BooleanField(blank=True, default=False, verbose_name='Pressão?')),
                ('alergia', models.BooleanField(blank=True, default=False, verbose_name='Alergia?')),
                ('doenca_sistemica', models.CharField(blank=True, max_length=300, verbose_name='Doença Sistêmica?')),
                ('medicamento', models.CharField(blank=True, max_length=300, verbose_name='Medicamentos?')),
            ],
        ),
    ]
