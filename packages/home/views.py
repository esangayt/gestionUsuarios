from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users:login')


class FechaMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        return context

class TemplatePruebaMixin(FechaMixin,TemplateView):
    template_name = 'home/mixin.html'

    def get_context_data(self, **kwargs):
        context = super(TemplatePruebaMixin, self).get_context_data(**kwargs)
        context['nombre'] = 'Juanito'
        return context