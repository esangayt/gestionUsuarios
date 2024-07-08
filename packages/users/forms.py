from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
            }
        )
    )

    password2 = forms.CharField(
        label='Repetir Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir Contraseña',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'gender']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
            # self.add_error('password2', 'Las contraseñas no coinciden')
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        required=True,
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Nombre de usuario',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Usuario o contraseña incorrectos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual',
            }
        )
    )

    new_password = forms.CharField(
        label='Nueva contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Nueva contraseña',
            }
        )
    )

    new_password2 = forms.CharField(
        label='Repetir nueva contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir nueva contraseña',
            }
        )
    )

    def clean_new_password2(self):
        new_password = self.cleaned_data['new_password']
        new_password2 = self.cleaned_data['new_password2']

        if new_password != new_password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return new_password2


class ValidateCodeForm(forms.Form):
    codregistro = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.pk = pk #recibe de las urls
        print("sss")
        super(ValidateCodeForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        print("---")
        codregistro = self.cleaned_data['codregistro']
        print("validado")
        if len(codregistro) != 6:
            raise forms.ValidationError('El código de registro debe tener 6 caracteres')

        if not User.objects.cof_validate(self.pk, codregistro):
            raise forms.ValidationError('El código de registro es incorrecto')

        return codregistro

