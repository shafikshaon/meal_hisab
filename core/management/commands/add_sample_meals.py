import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from meals.models import Meal


class Command(BaseCommand):
    help = 'Create new sample meals'

    def handle(self, *args, **kwargs):
        current_year = datetime.now().year
        current_month = datetime.now().month
        next_month = (datetime.today().replace(day=1) + timedelta(days=31)).month
        previous_month = (datetime.today().replace(day=1) - timedelta(days=1)).month

        for _day in range(1, 31):
            _current_month_date = str(current_year) + '-' + str(current_month) + '-' + str(_day)
            _previous_month_date = str(current_year) + '-' + str(previous_month) + '-' + str(_day)
            _next_month_date = str(current_year) + '-' + str(next_month) + '-' + str(_day)

            # user id 1
            Meal.objects.create(
                user_id=1,
                meal_date=_current_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

            Meal.objects.create(
                user_id=1,
                meal_date=_previous_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

            Meal.objects.create(
                user_id=1,
                meal_date=_next_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

            # user id 2
            Meal.objects.create(
                user_id=2,
                meal_date=_current_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

            Meal.objects.create(
                user_id=2,
                meal_date=_previous_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

            Meal.objects.create(
                user_id=2,
                meal_date=_next_month_date,
                breakfast=random.choice([0, 0.5, 1, 1.5, 2]),
                lunch=random.choice([0, 1, 2]),
                dinner=random.choice([0, 1, 2])
            )

        print("Sample meals added successfully!")
