from django.urls import path
from . import views

urlpatterns = [
    # Ensure there is no recursive include here
    path('', views.home, name='home'),  # Example path
]
