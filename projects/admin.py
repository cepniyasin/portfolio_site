from django.contrib import admin
from .models import JSProject, GisProject, PythonProject

# Register your models here.
admin.site.register(GisProject)
admin.site.register(PythonProject)
admin.site.register(JSProject)