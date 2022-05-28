from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.info(request, 'Feedback Received Thankyou!!')
        return render(request, 'contact.html')


class Blog(TemplateView):
    template_name = 'blog.html'


class BlogDetail(TemplateView):
    template_name = 'blog-single.html'
