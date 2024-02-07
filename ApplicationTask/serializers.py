from rest_framework import serializers
from .views import Task, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, data):
        category = Category.objects.create(**data)
        return category

    def update(self, instance, data):
        Category.objects.filter(id=instance.id).update(
            **data,
        )
        return instance


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, data):
        category_name = data.pop('category')['name']
        category = Category.objects.get(name=category_name)
        task = Task.objects.create(category=category, **data)
        return task

    def update(self, instance, data):
        category_name = data.pop('category')['name']
        category = Category.objects.get(name=category_name)
        Task.objects.filter(id=instance.id).update(
            category=category,
            **data,
        )
        return instance

