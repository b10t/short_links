from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from links.models import Links


@api_view(['POST'])
def create_short_link(request):
    if request.method == 'POST':

        return JsonResponse(dict(url='asdasdasd'), status=200)
