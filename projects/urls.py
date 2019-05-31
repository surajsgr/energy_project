from django.urls import path
from . import views

urlpatterns = [
    path("team_info/",views.team_info,name="team_info"),
    path("", views.project_index, name="project_index"),
    path("1/", views.project_detail, name="project_detail"),
    path("1/model/", views.energy,name='model'),
    path("1/visualisation/",views.visualisation,name="visualisation")
]