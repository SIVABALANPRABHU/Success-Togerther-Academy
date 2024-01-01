# main/urls.py

from django.urls import path
from .views import index, success_view  # Correct import

urlpatterns = [
    path('', index, name='index'),
    path('success/', success_view, name='success'),  # Use the correct function name
]
