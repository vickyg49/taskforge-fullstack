from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class FrontendAppView(TemplateView):
    template_name = "index.html"