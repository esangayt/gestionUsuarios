from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView, View
)

from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import (
    FormView
)
from packages.users.forms import UserRegisterForm, LoginForm
from packages.users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

# class CreaterUserView(CreateView):
#   template_name = 'users/create.html'
#  model = User
# form_class = UserRegisterForm
# success_url = reverse_lazy('users:create')
# success_url = "/"

class CreaterUserView(FormView):
    template_name = 'users/create.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home:welcome')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )

        return super().form_valid(form)


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
