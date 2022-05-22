from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.models import Contact


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return render(request, 'index.html')


class AboutUs(TemplateView):
    template_name = 'about.html'


class Services(TemplateView):
    template_name = 'services.html'


class Pricing(TemplateView):
    template_name = 'pricing.html'


class Cars(TemplateView):
    template_name = 'car.html'


class CarDetail(TemplateView):
    template_name = 'car-single.html'


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
