from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # ex: /
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
