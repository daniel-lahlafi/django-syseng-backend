from django.urls import include, path
from .views import get_quiz

urlpatterns = [
    path('quiz/<str:toolkit>', get_quiz)
]
