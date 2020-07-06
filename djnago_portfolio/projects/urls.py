from django.urls import path
from projects import views

app_name = 'projects'
# <int:pk> - used to capture urls path and int in converter pk is primary key id
urlpatterns = [
    path('', views.all_projects, name="all_projects"),
    path('<int:pk>', views.project_details, name="project_details"),
    path('home/', views.home, name="home"),
]

# app_name and name of path will be used to link urls templates
