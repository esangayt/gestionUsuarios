from django import forms

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

