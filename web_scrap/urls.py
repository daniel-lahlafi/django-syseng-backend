from django.urls import path
from web_scrap import views

urlpatterns = [
    path('update-toolkits', views.web_scrap, name="update-toolkits"),
    path('get-toolkit-names', views.get_toolkit_names),
    path('get-toolkit-url/<str:toolkit_name>', views.get_toolkit_url),
]