# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.generic import TemplateView


# class FrontendAppView(TemplateView):
#     template_name = "index.html"

from django.views import View
from django.http import FileResponse
import os
from django.conf import settings

class FrontendAppView(View):
    def get(self, request):
        return FileResponse(
            open(os.path.join(settings.BASE_DIR, "frontend_dist/app/index.html"), "rb"),
            content_type="text/html"
        )

