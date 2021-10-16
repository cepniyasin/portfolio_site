"""genericsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, projects_view, bj_view


from projects.views import (
    gis_dynamic_lookup_view,
    gis_project_list_view,
    python_dynamic_lookup_view,
    python_project_list_view,
    js_dynamic_lookup_view,
    js_project_list_view
)



from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('projects/', projects_view, name='projects'),
    path('blackjack/', bj_view, name='blackjack'),

    path('GISprojects/', gis_project_list_view, name='gis-list'),
    path('GISprojects/<int:my_id>/', gis_dynamic_lookup_view, name='project-detail'),

    path('Python_projects/', python_project_list_view, name='python-list'),
    path('Python_projects/<int:my_id>/', python_dynamic_lookup_view, name='project-detail'),

    path('JSprojects/', js_project_list_view, name='js-list'),
    path('JSprojects/<int:my_id>/', js_dynamic_lookup_view, name='project-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)