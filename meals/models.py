from django.db import models

from accounts.models import User
from core.models import Status, TimeLog


class Meal(TimeLog, Status):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals_user')
    meal_date = models.DateField(blank=False, null=False)
    breakfast = models.FloatField(default=0.5)
    lunch = models.FloatField(default=1)
    dinner = models.FloatField(default=1)

    class Meta:
        app_label = "meals"
        db_table = "meals_meals"
        verbose_name = "meals_meal"
        verbose_name_plural = "meals_meals"
