from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet, home

router = routers.DefaultRouter()
router.register(r'Tasks', TaskViewSet)
router.register(r'Categories', CategoryViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
]
