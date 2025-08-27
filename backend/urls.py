from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from .views import frontend_index  # function-based view

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', frontend_index, name='home')  # serve Ember index.html
]


# from django.http import HttpResponse
# from django.urls import path

# def test(request):
#     return HttpResponse("Hello World!")

# urlpatterns = [
#     path('', test),
# ]