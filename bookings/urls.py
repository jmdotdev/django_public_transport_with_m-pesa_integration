from django.urls import path

from bookings.views import BookingForm,TicketPage

urlpatterns = [
    path('<int:pk>/', BookingForm.as_view(), name='BookingForm'),
    path('TicketPage/<int:pk>/', TicketPage.as_view(), name='TicketPage')
]
