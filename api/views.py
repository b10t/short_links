from django.core.exceptions import ValidationError
from django.http import JsonResponse
from links.models import Links
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_short_link(request):
    if request.method == 'POST':
        if 'url' in request.data:
            url = request.data['url']

            try:
                link, _ = Links.objects.get_or_create(link=url)
            except ValidationError as e:
                return JsonResponse(
                    dict(error=e.message),
                    status=200
                )

            return JsonResponse(
                dict(url=request.build_absolute_uri(f'/l_{link.link_id}/')),
                status=200
            )
        else:
            return JsonResponse(
                dict(error='Ошибка формата данных.'),
                status=200
            )
