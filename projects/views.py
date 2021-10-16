from .models import JSProject, GisProject, PythonProject
from django.http import Http404
from django.shortcuts import render, get_object_or_404


# Create your views here.

def gis_project_list_view(request):
    queryset = GisProject.objects.all()
    context = {
        "object_list": queryset
    }
    return render (request, "projects/project_list.html", context)


def gis_dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(GisProject, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "projects/project_detail.html", context)


def python_project_list_view(request):
    queryset = PythonProject.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "projects/project_list.html", context)


def python_dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(PythonProject, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "projects/project_detail.html", context)



def js_project_list_view(request):
    queryset = JSProject.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "projects/project_list.html", context)


def js_dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(JSProject, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "projects/project_detail.html", context)

