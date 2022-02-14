from django.db import models
from ckeditor.fields import RichTextField

class Assignment(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    def set_title(self, title):
        self.title = title

    @classmethod
    def validation_error_message(self):
        return "Assignment not added. Title can not have more than 20 characters"

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title
