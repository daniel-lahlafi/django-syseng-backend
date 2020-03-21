from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('quiz', views.quiz, name="quiz")
]