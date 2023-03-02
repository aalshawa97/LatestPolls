import os
import django

from pages.views import createPageView

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.contrib import admin
from django.urls import path, include

from pages import views as poll_views

urlpatterns = [
    #path("", views.index, name='index'),
    #Home
    path('', include('pages.urls')),
    #Django adminstration
    path('admin/', admin.site.urls),
    path('create/', createPageView, name='create'),
    #path('vote', poll_views.votePageView('',0), name='vote'),
    #path('', poll_views.homePageView, name='home')
    #path('', pages.templates)
    #path('about/', views.about, name='about'),
]
