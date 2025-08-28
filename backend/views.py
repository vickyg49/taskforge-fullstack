# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.generic import TemplateView


# class FrontendAppView(TemplateView):
#     template_name = "index.html"

from django.http import FileResponse
import os
from django.conf import settings

def frontend_index(request):
    # Path to your built index.html
    file_path = os.path.join(settings.BASE_DIR, "frontend_dist", "app", "index.html")
    return FileResponse(open(file_path, 'rb'))

