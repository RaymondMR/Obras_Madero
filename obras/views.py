from django.shortcuts import render
from .models import  Obra
from django.http import Http404
from django.views.generic import DetailView, ListView


class ObrasListView(ListView):
    model=Obra
    context_object_name="obras"
    template_name="obras/obras_list.html"

class ObrasDetailView(DetailView):
    model=Obra
    context_object_name="obra"
    template_name="obras/obra_detail.html"



