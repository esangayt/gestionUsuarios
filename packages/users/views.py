from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)
from django.views.generic.edit import (
    FormView
)
from packages.users.forms import UserRegisterForm
from packages.users.models import User


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
