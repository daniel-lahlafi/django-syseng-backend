from django.urls import path
from web_scrap import views

urlpatterns = [
    path('update-toolkits', views.web_scrap)
]