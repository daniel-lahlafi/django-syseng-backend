from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from web_scrap.models import Toolkit
from .models import Quiz

def get_quiz(request, toolkit):
    toolkit = get_object_or_404(Toolkit, name=toolkit)

    quizzes = Quiz.objects.filter(toolkit=toolkit)
    result = list()
    for quiz in quizzes:
        result.append(
            {
                'question': quiz.question,
                'answer_1': quiz.answer_1,
                'answer_2': quiz.answer_2,
                'answer_3': quiz.answer_3,
                'answer_4': quiz.answer_4,
                'correct_answer': quiz.correct_answer
            }
        )

    response = JsonResponse({
        'result': result
    })
    return response