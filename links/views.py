from django.http import HttpResponseRedirect
from django.shortcuts import render


def redirect(request, path):
    return HttpResponseRedirect('https://ya.ru')
