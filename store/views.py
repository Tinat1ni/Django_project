from django.shortcuts import render
from django.http import HttpResponse

def store_view(request):
    return HttpResponse('Store page with products')

def second_store_view(request):
    return HttpResponse('here will be list of specific products')