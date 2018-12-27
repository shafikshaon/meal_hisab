from django.urls import path
from django.views.generic import TemplateView

from meals.views import MealListView, MealCreateView

urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('warning/', TemplateView.as_view(template_name='meals/warning.html'), name='meal-warning'),
]
