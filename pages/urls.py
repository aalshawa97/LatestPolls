from django.contrib import admin
from django.urls import path

from pages.views import homePageView, aboutPageView, createPageView, votePageView, resultsPageView
#from poll import views as poll_views
urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", homePageView, name="home"),
    path("about/", aboutPageView, name='about'),
    path("create/", createPageView, name='create'),
    path("vote<poll_id>/", votePageView, name='vote'),
    path('<int:question_id>/results/', resultsPageView, name='results'),
]
