import requests
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DeleteView

from bookings.models import Booking
from core.forms import ReserveSeatForm
from core.models import Route


class BookingForm(View):
    def get(self, request, pk):
        route = Route.objects.get(pk=pk)
        form = ReserveSeatForm(request.POST)
        return render(request, 'BookingForm.html', {'form': form})

    def post(self, request, pk):
        route = Route.objects.get(pk=pk)
        form = ReserveSeatForm(request.POST)
        if form.is_valid():
            form.instance.route = route
            persons = form.cleaned_data.get('persons')
            form.instance.total = route.price * persons
            var_mobile = form.cleaned_data.get('mobile_no')
            final_mobile = var_mobile.replace("0", "254", 1)
            form.instance.mobile_no = final_mobile
            form.instance.user = self.request.user
            obj = form.save()
        else:
            return render(request, 'BookingForm.html', {'form': form})
        if not route.car.booked:
            persons = form.cleaned_data.get('persons')
            route.car.capacity -= persons
            route.car.save()
        if route.car.booked & route.car.capacity > 0:
            persons = form.cleaned_data.get('persons')
            route.car.capacity -= persons
            route.car.save()
            return render(request, 'BookingForm.html', {'form': form})
        return redirect('BookingDetailsPage', obj.pk)


class BookingDetailsPage(TemplateView):
    template_name = 'Booking_Details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking'] = Booking.objects.get(pk=self.kwargs.get('pk'))
        return context


class MyBookings(View):
    def get(self, request):
        booking = Booking.objects.filter(user=self.request.user)
        return render(request, 'MyBookings.html', {'booking': booking})

    def post(self, request):
        var_domain = request.build_absolute_uri('/')[:-1]
        domain = var_domain + '/mpesa/submit/'
        booking = Booking.objects.get(id=request.POST['booking_id'])
        res = requests.post(url=domain,
                            data={'phone_number': booking.mobile_no, 'amount': booking.total})
        return redirect('/')


class CancelBooking(View):
    def get(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        var_persons = booking.persons
        return_booked_seats_to_car = var_persons
        booking.route.car.capacity += return_booked_seats_to_car
        booking.route.car.save()
        booking.delete()
        messages.info(request, 'Booking deleted Successfully')
        return render(request, 'MyBookings.html')
