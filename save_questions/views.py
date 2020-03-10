from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from web_scrap.models import Toolkit

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing saved questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(toolkit = get_object_or_404(Toolkit, name=self.request.data.get('toolkit')))
    