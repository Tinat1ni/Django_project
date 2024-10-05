from django.shortcuts import render
from django.http import HttpResponse

def order_view(request):
    return HttpResponse('on this page users can make orders')

def second_order_view(request):
    return HttpResponse('and here will be list of orders')

