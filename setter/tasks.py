from django.conf import settings
from background_task import background

from .models import Assignment


@background(schedule=settings.HARD_DELETE_TIMER)
def schedule_hard_delete_assignment(pk):
    """Background process to hard delete assignment after few seconds."""
    try:
        assignment = Assignment.deleted_objects.get(id=pk)
        assignment.hard_delete()
    except:
        pass
