from django.urls import path
from . import views

urlpatterns = [
    path("boards/<slug:slug>/", views.Thread.as_view(), name="thread")
]