from django.contrib import admin

from .models import Question, Assignment

class SoftDeletionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = self.model.all_objects
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def delete_model(self, request, instance):
        instance.hard_delete()

    def delete_queryset(self, request, instance_set):
        for instance in instance_set:
            instance.hard_delete()

admin.site.register(Question, SoftDeletionAdmin)
admin.site.register(Assignment, SoftDeletionAdmin)
