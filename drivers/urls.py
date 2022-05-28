from django.urls import path

from drivers.views import DriversView

urlpatterns = [
    path('', DriversView.as_view(), name='DriversView')
]
