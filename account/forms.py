from django import forms
from django.contrib.auth import get_user_model

from core.mail import send_mail_template
from core.utils import generate_hash_key

from django.contrib.auth.forms import AuthenticationForm


from .models import PasswordReset

User = get_user_model()


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    password2 = forms.CharField(label='Confirmar Senha',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nome de usuário já existe!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            print(f'Email ja cadastrado! {email}')
            raise forms.ValidationError('Email ja cadastrado!')
        print(f'email ok! {email}')
        return email

    #confere se o campo de senha1 é igual ao campo de senha2
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            print('password1:' + password1)
            print('password2:' + password2)
            raise forms.ValidationError('')
        return password2

    #validando o campo de senha1
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        minimal_len_char = 8

        if len(password1) < minimal_len_char:
            raise forms.ValidationError(
                f'• Mínimo {minimal_len_char} caracteres!')
        return password1

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'email': forms.TextInput(attrs={'placeholder': 'exemplo@exemplo.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
        }


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username ou E-mail',
                                                             'autocomplete': 'off'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username) != username:
            raise forms.ValidationError('Usuário errado ou não existe!')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if User.objects.filter(password=password).exists():
            raise forms.ValidationError('Senha i!')
        return password


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário encontrado com este e-mail'
        )

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'password_reset_mail.html'
        subject = 'Criar nova senha'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])
