import os

import django

from pages.views import createPageView

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Home
    path('', include('pages.urls')),
    #Django adminstration
    path('admin/', admin.site.urls),
    path('create/', createPageView, name='create'),
]
