from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)


class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

