from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from core.forms import AddFriverForm


class DriversView(FormView):
    template_name = 'Add_driver.html'
    form_class = AddFriverForm
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
