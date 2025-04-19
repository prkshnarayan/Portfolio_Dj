from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    # your other URLs...
]
