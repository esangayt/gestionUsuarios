from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users:login')


class MixinP(object):
    def get_context_data(self, **kwargs):
        print("mixin")
        context = super(MixinP, self).get_context_data(**kwargs)
        context['nombre 2'] = 'Juanito 2'
        return context


class FechaMixin(object):
    def get_context_data(self, **kwargs):
        print("fecha")
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        return context


class TemplatePruebaMixin(FechaMixin, MixinP, TemplateView):
    template_name = 'home/mixin.html'

    def get_context_data(self, **kwargs):
        print("nombre")
        context = super(TemplatePruebaMixin, self).get_context_data(**kwargs)
        context['nombre'] = 'Juanito'
        return context
