from django.urls import path, include

from . import views

urlpatterns = [
    path("", include("allauth.urls")),
    path("loggedout/", views.LoggedOut.as_view(), name="logged_out"),
]
