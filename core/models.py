from django.db import models


class Status(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TimeLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
