from django import forms
from .models import Profile, Endereco


class ProfileForm(forms.Model):
    
    class Meta:
        model = Profile
        fields = ['sexo_choices', 'full_name', 'cpf', 'rg', 'birth_date']
        
class EnderecoForm(forms.Model):
    
    class Meta:
        model = Endereco
        fields = ['']