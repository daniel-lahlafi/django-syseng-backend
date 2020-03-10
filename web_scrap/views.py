from django.shortcuts import render
from .web_scrapper import getToolkit
from .models import Toolkit
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def web_scrap(request):
    if request.data.get('overwrite') == "True":
        for toolkit in Toolkit.objects.all():
            toolkit.content = ""
            toolkit.save()

    for toolkit in Toolkit.objects.all():
        if toolkit.content == "":
            toolkit.content = getToolkit(toolkit.url, toolkit.name)
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