from django.urls import path
from . import views

app_name = 'booksite'

urlpatterns = [
    path("",views.homepage, name="homepage"),
]