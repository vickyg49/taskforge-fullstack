from django.contrib import admin
from django.urls import path, include
from tasks.views import TaskViewSet
from .views import frontend_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # API routes
    path('', frontend_index, name='home'),  # Ember frontend
]



# from django.http import HttpResponse
# from django.urls import path

# def test(request):
#     return HttpResponse("Hello World!")

# urlpatterns = [
#     path('', test),
# ]