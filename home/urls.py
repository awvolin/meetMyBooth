from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    #path("compute/<int:value>", views.compute, name="compute"),
    path("launch", views.launch, name="launch")
]