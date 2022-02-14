from django.db import models
from ckeditor.fields import RichTextField

class Assignment(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title
