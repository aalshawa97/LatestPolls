import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
from .views import homePageView, createPageView, resultsPageView
from django.test import RequestFactory


def test_my_test():
    request = RequestFactory().get('/')
    response = homePageView(request)
    # Success return code
    assert response.status_code == 200


def test_create_view():
    request = RequestFactory().get('/')
    response = createPageView(request)
    assert response.status_code == 200

def test_results_view():
    request = RequestFactory().get('/')
    response = resultsPageView(request, 1)
    assert response.status_code == 200