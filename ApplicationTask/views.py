from rest_framework import viewsets, permissions
from django.http import HttpResponse
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def home(request):
    return HttpResponse("For api accuses use /api.")
