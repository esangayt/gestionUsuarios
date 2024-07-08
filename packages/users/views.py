from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView, View
)
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import (
    FormView
)
from packages.users.forms import UserRegisterForm, LoginForm, UpdatePasswordForm, ValidateCodeForm
from packages.users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from .functions import code_generator


# class CreaterUserView(CreateView):
#   template_name = 'users/create.html'
#  model = User
# form_class = UserRegisterForm
# success_url = reverse_lazy('users:create')
# success_url = "/"

class CreaterUserView(FormView):
    template_name = 'users/create.html'
    form_class = UserRegisterForm
    # success_url = reverse_lazy('home:welcome')
    success_url = '/'
    def form_valid(self, form):
        # generamos el código
        codigo = code_generator()

        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            codregistro=codigo
        )

        # enviamos el correo
        send_mail(
            'Confirmar registro',
            'Tu código de registro es: {}'.format(codigo),
            'esangayt_19@unc.edu.pe',
            [form.cleaned_data['email']]
        )

        #redirigir a pantalla de validación
        return HttpResponseRedirect(
            reverse('users:user_verification', kwargs={
                'pk': user.id
            })
        )
        # return super().form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:welcome')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super().form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users:login'))


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users:login')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = self.request.user
        password = form.cleaned_data['password']

        user = authenticate(username=user.username, password=password)

        #error if authenticate fails
        if not user:
            form.add_error('password', 'Contraseña actual incorrecta')
            return self.form_invalid(form)

        if user:
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()

        logout(self.request)

        return super().form_valid(form)


class ValidateCodeView(FormView):
    template_name = 'users/validate.html'
    form_class = ValidateCodeForm
    success_url = reverse_lazy('users:login')

    def get_form_kwargs(self):
        print("--------------------")
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
        })

        return kwargs

    def form_valid(self, form):
        user_id = self.kwargs['pk']
        codigo = form.cleaned_data['codregistro']

        user = User.objects.get(id=user_id, codregistro=codigo)
        user.is_active = True
        user.save()

        return super().form_valid(form)