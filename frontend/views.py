from django.shortcuts import render

def home(request):
    return render(request, 'frontend/chat.html')

def quiz(request):
    return render(request, 'frontend/quiz.html')