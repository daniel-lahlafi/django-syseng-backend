from django.shortcuts import render, get_object_or_404
from .web_scrapper import getToolkit
from .models import Toolkit
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def web_scrap(request):
    if request.data.get('overwrite') == "true":
        for toolkit in Toolkit.objects.all():
            toolkit.content = ""
            toolkit.save()

    for toolkit in Toolkit.objects.all():
        if toolkit.content == "":
            toolkit.content = getToolkit(toolkit.url)
            toolkit.save()

    response = JsonResponse(
        {
            'result': 'Completed'
        }
    )

    return response

@api_view(['GET'])
def get_toolkit_names(request):
    toolkit_names = [toolkit.name for toolkit in Toolkit.objects.all()]
    response = JsonResponse(
        {
            'toolkit_names': toolkit_names
        }
    )
    return response

@api_view(['GET'])
def get_toolkit_url(request, toolkit_name):
    toolkit = get_object_or_404(Toolkit, name=toolkit_name)
    response = JsonResponse(
        {
            'toolkit_name': toolkit.name,
            'url': toolkit.url
        }
    )
    return response