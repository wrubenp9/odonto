from django.urls import path
from . import views


app_name = 'form'

urlpatterns = [
    path('anamnese/', views.anamnese , name='anamnese')
    
]
