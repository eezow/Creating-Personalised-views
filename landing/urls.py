from django.urls import path
from landing import views

urlpatterns = [
    path('', views.LandingEndpoint.as_view(), name='landing'),
]