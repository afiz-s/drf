from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default='')
    parent_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']