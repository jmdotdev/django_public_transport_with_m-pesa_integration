from django.urls import path

from bookings.views import BookingForm,TicketPage

urlpatterns = [
    path('<int:pk>/', BookingForm.as_view(), name='BookingForm'),
    path('TicketPage/', TicketPage.as_view(), name='TicketPage')
]
