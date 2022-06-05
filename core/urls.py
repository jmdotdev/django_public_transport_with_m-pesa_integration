from django.urls import path

from core.views import HomePage, AboutUs, Services, Routes, Cars, \
    CarDetail, ContactUs, RoutesDetail, AddTestimonials, AddCar,UpdateCar

urlpatterns = [
    path('', HomePage.as_view(), name="HomePage"),
    path('AboutUs/', AboutUs.as_view(), name="AboutUs"),
    path('Services/', Services.as_view(), name="Services"),
    path('Routes/', Routes.as_view(), name="Routes"),
    path('RoutesDetail/<int:pk>/', RoutesDetail.as_view(), name="RoutesDetail"),
    path('Cars/', Cars.as_view(), name="Cars"),
    path('AddCar/', AddCar.as_view(), name="AddCar"),
    path('UpdateCar/<int:pk>/', UpdateCar.as_view(), name="UpdateCar"),
    path('CarDetail/<int:pk>/', CarDetail.as_view(), name="CarDetail"),
    path('ContactUs/', ContactUs.as_view(), name="ContactUs"),
    path('AddTestimonials/', AddTestimonials.as_view(), name="AddTestimonials"),
]
