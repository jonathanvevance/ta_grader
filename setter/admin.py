from django.contrib import admin

from .models import Question, Assignment

admin.site.register(Question)
admin.site.register(Assignment)
