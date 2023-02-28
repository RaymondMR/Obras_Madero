from django.urls import path
from . import views

urlpatterns=[
path('', views.ObrasListView.as_view(), name="obras.list"),
path('<int:pk>', views.ObrasDetailView.as_view(), name="obra_detail"),
]
