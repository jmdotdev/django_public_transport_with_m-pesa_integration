from django.contrib import admin

# Register your models here.
from core.models import Car, Contact, Testimonial, Route

admin.site.register(Car)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Route)
