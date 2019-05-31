from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("2/", views.solar_detail, name="solar_detail"),
    path("2/model", views.solar_model,name='solar_model'),
    path("2/visualisation",views.visualisation,name="solar_visualisation"),

]