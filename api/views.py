from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from links.models import Links


@api_view(['POST'])
def create_short_link(request):
    if request.method == 'POST':
        if 'url' in request.data:
            link, _ = Links.objects.get_or_create(
                link=request.data['url'])
            return JsonResponse(
                dict(
                    url=request.build_absolute_uri(f'/{link.link_id}/')
                ),
                status=200
            )
        else:
            return JsonResponse(dict(error='Ошибка формата данных.'), status=200)
