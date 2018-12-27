from django.urls import path
from django.views.generic import TemplateView

from meals.views import MealListView, MealCreateView, MealUpdateView, MealDeleteView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('update/<pk>', MealUpdateView.as_view(), name="meal-update"),
    path('delete/<pk>', MealDeleteView.as_view(), name="meal-delete"),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('warning/', TemplateView.as_view(template_name='meals/warning.html'), name='meal-warning'),
]
