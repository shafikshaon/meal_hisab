import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from meals.forms import AddMealForm, UpdateMealForm
from meals.models import Meal


class MealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add.html'
    form_class = AddMealForm
    login_url = '/accounts/login/'

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        messages.success(self.request, 'Meal was added successfully.')
        messages.set_level(self.request, None)
        return HttpResponseRedirect(reverse('meal-add'))

    def dispatch(self, *args, **kwargs):
        is_added_meal = Meal.objects.filter(meal_date=datetime.datetime.today(), user_id=self.request.user.pk)
        if is_added_meal:
            return HttpResponseRedirect(reverse('meal-warning'))
        return super().dispatch(*args, **kwargs)


class MealUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'meals/update.html'
    model = Meal
    form_class = UpdateMealForm
    login_url = '/accounts/login/'

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        messages.success(self.request, 'Meal was updated successfully.')
        return HttpResponseRedirect(reverse('meal-update', kwargs={'pk': meal.pk}))


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
