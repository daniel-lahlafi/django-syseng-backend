from django.urls import include, path
from nlp_search import views

urlpatterns = [
    path('search', views.question_query_post),
    path('sentiment', views.sentiment_analysis_post)
]
