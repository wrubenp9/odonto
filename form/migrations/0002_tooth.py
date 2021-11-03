# Generated by Django 3.2.8 on 2021-11-02 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tooth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, verbose_name='Número do dente')),
                ('report', models.CharField(blank=True, max_length=300, verbose_name='Relatório')),
                ('anamnese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dente', to='form.anamnese')),
            ],
        ),
    ]