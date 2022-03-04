from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from links.models import Links
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_short_link(request):
    if request.method == 'POST':
        if 'url' in request.data:
            url = request.data['url']

            try:
                URLValidator()(url)
            except ValidationError as e:
                return JsonResponse(
                    dict(
                        error=e.message
                    ),
                    status=200
                )

            link, _ = Links.objects.get_or_create(
                link=url)
            return JsonResponse(
                dict(
                    url=request.build_absolute_uri(f'/{link.link_id}/')
                ),
                status=200
            )
        else:
            return JsonResponse(dict(error='Ошибка формата данных.'), status=200)
