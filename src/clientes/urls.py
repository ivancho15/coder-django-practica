from django.urls import path

from clientes import views

app_name = "clientes"

urlpatterns = [

    path('', views.index, name="index" ),
]
