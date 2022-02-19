from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from .soft_deletion import SoftDeletionModel

class Assignment(SoftDeletionModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def set_title(self, title):
        self.title = title

    @classmethod
    def validation_error_message(self, e):

        error_message = e.messages[0]
        if "Ensure this value has" in error_message:
            return "Title must be at most 100 characters"
        elif error_message == "Assignment with this Title already exists.":
            return "Assignment with this title already exists"
        elif error_message == "This field cannot be blank.":
            return "Assignment title can not be blank"

        return "Unknown error :/"

class Question(SoftDeletionModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=100)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title
