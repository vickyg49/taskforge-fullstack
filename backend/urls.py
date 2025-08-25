from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from .views import index
from .views import EmberAppView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # -> exposes /api/tasks/
    re_path(r'^(?!api/).*$', EmberAppView.as_view(), name='ember-app')
]
