from django.http import JsonResponse
from django.shortcuts import render

def index(_request):
    return render(request, 'index.html')