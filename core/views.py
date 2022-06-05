from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, UpdateView

from core.forms import AddCarForm
from core.models import Contact, Car, Testimonial, Route


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        return context


class AboutUs(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['testimonial'] = Testimonial.objects.all()
        return context


class Services(TemplateView):
    template_name = 'services.html'


class Routes(TemplateView):
    template_name = 'Routes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = Route.objects.all()
        return context


class RoutesDetail(DetailView):
    template_name = 'Routes_Detail.html'
    model = Route

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = Route.objects.get(pk=self.kwargs.get('pk'))
        return context


class Cars(TemplateView):
    template_name = 'car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.all()
        return context


class CarDetail(DetailView):
    template_name = 'car-single.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs.get('pk'))
        return context


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        contacts = Contact()
        contacts.save_contacts(request=request)
        return render(request, 'contact.html')


class AddTestimonials(View):
    def get(self, request):
        return render(request, 'add_testimonial.html')

    def post(self, request):
        testimonial = Testimonial()
        testimonial.save_testimonial(request=request)
        return render(request, 'add_testimonial.html')


class AddCar(FormView):
    template_name = 'add_car.html'
    success_url = '/'
    messages = 'Car added successfully'
    form_class = AddCarForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


class UpdateCar(UpdateView):
    model = Car
    fields = ['name', 'image', 'capacity', 'fuel', 'plate_no', 'Transmission', 'description']
    template_name = 'update_car_details.html'
    messages = 'Car updated successfully'
    success_url = '/'
