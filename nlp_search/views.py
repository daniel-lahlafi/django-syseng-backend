from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from save_questions.models import Question
from save_questions.serializers import QuestionSerializer
from nlp_search.transformer import question_transformer, sentiment_transformer
from rest_framework.decorators import api_view
from web_scrap.models import Toolkit

@api_view(['POST'])
def question_query_post(request):
    question = request.data.get('question')
    toolkit_name = request.data.get('toolkit_name')
    attempt = request.data.get('attempt')

    toolkit = get_object_or_404(Toolkit, name=toolkit_name)
    try:
        answer = Question.objects.get(question=question).answer
    except:
        answer = question_transformer(question, toolkit.content, attempt)
    
    response = JsonResponse(
        {
            'question': question,
            'toolkit_name': toolkit_name,
            'answer': answer
        }
    )

    return response

@api_view(['POST'])
def sentiment_analysis_post(request):
    text_input = request.data.get('text')
    answer = sentiment_transformer(text_input)

    response = JsonResponse(
        {
            'text': text_input,
            'answer': answer
        }
    )

    return response