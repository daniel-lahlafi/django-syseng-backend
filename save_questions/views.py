from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing saved questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    