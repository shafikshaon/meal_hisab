import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from meals.models import Meal


class MealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/list.html'
    login_url = '/accounts/login/'
    model = Meal

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Meal.objects \
            .select_related('user') \
            .filter(user_id=self.request.user.pk, meal_date__month=current_month) \
            .order_by('meal_date')
        return context
