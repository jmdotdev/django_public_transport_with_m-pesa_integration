from django.urls import path

from core.views import HomePage, AboutUs, Services, Routes, Cars, CarDetail, ContactUs, Blog,BlogDetail,RoutesDetail

urlpatterns = [
    path('', HomePage.as_view(), name="HomePage"),
    path('AboutUs/', AboutUs.as_view(), name="AboutUs"),
    path('Services/', Services.as_view(), name="Services"),
    path('Routes/', Routes.as_view(), name="Routes"),
    path('RoutesDetail/<int:pk>/', RoutesDetail.as_view(), name="RoutesDetail"),
    path('Cars/', Cars.as_view(), name="Cars"),
    path('CarDetail/<int:pk>/', CarDetail.as_view(), name="CarDetail"),
    path('ContactUs/', ContactUs.as_view(), name="ContactUs"),
    path('Blog/', Blog.as_view(), name="Blog"),
    path('BlogDetail/', BlogDetail.as_view(), name="BlogDetail"),
]
