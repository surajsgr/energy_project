from django.urls import path
from . import views

urlpatterns = [
    # path("", views.project_index, name="project_index"),
    path("3/", views.wind_detail, name="wind_detail"),
    path("3/model", views.wind_model,name='wind_model'),
    path("3/visualisation",views.wind_visualisation,name="wind_visualisation"),

]