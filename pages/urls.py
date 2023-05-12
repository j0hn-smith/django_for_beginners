from pages.views import HomePageTemplateView, AboutPageView
from django.urls import path

app_name = "pages"
urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
