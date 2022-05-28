from django.urls import path

from accounts.views import Login

urlpatterns = [
    path('Login/', Login.as_view(), name='Login')
]
