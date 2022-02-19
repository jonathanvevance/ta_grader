from django.db import models
from django.utils import timezone

class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.mode = kwargs.pop('mode', 'alive-only')
        assert self.mode in ['all', 'alive-only', 'deleted-only']
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.mode == 'alive-only':
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        elif self.mode == 'deleted-only':
            return SoftDeletionQuerySet(self.model).exclude(deleted_at=None)
        elif self.mode == 'all':
            return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager(mode='alive-only')
    all_objects = SoftDeletionManager(mode='all')
    deleted_objects = SoftDeletionManager(mode='deleted-only')

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()
