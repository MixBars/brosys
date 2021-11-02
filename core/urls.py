from django.urls import path, include
from .views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('app', app, name='app')
]
