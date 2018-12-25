from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import TimeLog, Status


class User(AbstractUser, TimeLog, Status):
    email = models.EmailField(blank=False, null=False)
    is_admin = models.BooleanField(default=False, null=False, blank=False)
    member_from = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        app_label = "accounts"
        db_table = "accounts_users"
        verbose_name = "accounts_user"
        verbose_name_plural = "accounts_users"
