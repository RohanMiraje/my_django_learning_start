from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project


# Create your views here.

def project_list(request):
    return render(request, 'index.html')


def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()  # ORM to fetch objects from model created in Projects app
    return render(request, 'all_projects.html',
                  {'projects': projects})


# <!--                        <a> herf= "{% url 'app_name:name' arg_value %}"   this helps to link urls using names and args by retrieving correct urls</a>-->

def project_details(request, pk):
    # query the db to return one project objects using pk == id
    project = Project.objects.get(pk=pk)  # ORM to fetch object from model created in Projects app having id as pk
    # keyword below is project to be used inside template structure in html files
    return render(request, 'details.html',
                  {'project': project})


def home(request):
    return render(request, 'home.html')
