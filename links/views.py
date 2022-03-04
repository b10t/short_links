from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Links


def redirect(request, path):
    try:
        link = Links.objects.get(link_id=path)
    except Links.DoesNotExist:
        return HttpResponse(status=404)

    return HttpResponseRedirect(link.link)
