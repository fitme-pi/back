from django import forms

from core.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        # fields = ('nome''data_nascimento''email')
        exclude = ()
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo', 'autofocus': ''}),
            'data_nasc': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'youremail@email.com'}),
            'senha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '******', 'autofocus': ''}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'M ou F', 'autofocus': ''})
        }