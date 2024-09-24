from django.urls import path

from home.views import HomePageView

app_name = "home"
urlpatterns = [
    # ex: /
    path("", HomePageView.as_view(), name="index"),
]
