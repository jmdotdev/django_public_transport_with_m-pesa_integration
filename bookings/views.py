from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

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
        return redirect('TicketPage', obj.pk)


class TicketPage(TemplateView):
    template_name = 'TicketPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking'] = Booking.objects.filter(pk=self.kwargs.get('pk'))
        return context
