from django.shortcuts import render
from .models import  Obra
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from urllib.parse import quote_plus
from django.views.generic import TemplateView


class ObrasListView(LoginRequiredMixin, ListView):
    model=Obra
    context_object_name="obras"
    template_name="obras/obras_list.html"
    login_url = 'restricted_area'

class ObrasDetailView(LoginRequiredMixin, DetailView):
    model=Obra
    context_object_name="obra"
    template_name="obras/obra_detail.html"
    login_url = 'restricted_area'

class RestrictedAreaView(TemplateView):
    template_name="obras/area_restringida.html"
      


#class AuthorizedView(LoginRequiredMixin,TemplateView):
#   template_name="obras/area_restringida.html"
    