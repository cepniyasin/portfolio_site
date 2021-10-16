from django.http import HttpResponse
from django.shortcuts import render
from projects.models import JSProject, GisProject, PythonProject



# Create your views here.

def home_view(request, *args, **kwargs):
    queryset1 = GisProject.objects.all()
    queryset2 = PythonProject.objects.all()
    queryset3 = JSProject.objects.all()

    context1 = {
        "object_list": queryset1
    }
    context2 = {
        "object_list": queryset2
    }
    context3 = {
        "object_list": queryset3
    }

    context = {"gis":context1, "python":context2,"js":context3}
    return render(request, "home.html", context)
    # return render(request, "home.html")


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {} )


def projects_view(request, *args, **kwargs):
    return render(request, "projects.html", {})

def bj_view(request, *args, **kwargs):
    return render(request, "blackjack.html", {})