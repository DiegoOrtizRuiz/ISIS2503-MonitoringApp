from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('passwords/', views.password_list, name='passwordsList'),
    path('passwordCreate/', csrf_exempt(views.password_create), name='passwordCreate'),
]