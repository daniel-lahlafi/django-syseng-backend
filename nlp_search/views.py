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
    attempt = int(request.data.get('attempt'))
    is_saved_answer = False

    toolkit = get_object_or_404(Toolkit, name=toolkit_name)
    try:
        answer = Question.objects.get(question=question, toolkit=toolkit).answer
        is_saved_answer = True
    except:
        answer = question_transformer(question, toolkit.content, attempt)

    sentiment = sentiment_transformer(question)
    
    response = JsonResponse(
        {
            'question': question,
            'toolkit_name': toolkit_name,
            'answer': answer,
            'is_saved_answer': is_saved_answer, 
            'sentiment': [
                {
                    'label': sentiment.get('label'),
                    'score': str(sentiment.get('score'))
                }
            ]

        }
    )

    return response

@api_view(['POST'])
def sentiment_analysis_post(request):
    text_input = request.data.get('text')
    sentiment = sentiment_transformer(text_input)

    response = JsonResponse(
        {
            'text': text_input,
            'answer': [
                {
                    'label': sentiment.get('label'),
                    'score': str(sentiment.get('score'))
                }              
            ]
        }
    )

    return response