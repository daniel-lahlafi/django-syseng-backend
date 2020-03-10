from django.urls import path
from web_scrap import views

urlpatterns = [
    path('update-toolkits', views.web_scrap),
    path('get-toolkit-names', views.get_toolkit_names)
]