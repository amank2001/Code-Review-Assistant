from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_code, name='review_code'),
]