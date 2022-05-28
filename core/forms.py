from django import forms

from bookings.models import Booking
from drivers.models import Driver


class AddFriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control'}),
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Second_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'feedback': forms.TextInput(attrs={'class': 'form-control'}),
            'Avatar': forms.FileInput()
        }
        fields = '__all__'


class ReserveSeatForm(forms.ModelForm):
    class Meta:
        model = Booking
        # widgets = {
        #     'route': forms.TextInput(attrs={'class': 'form-control'}),
        #     'date': forms.DateInput(attrs={'class': 'form-control'}),
        #     'Time': forms.TimeInput(attrs={'class': 'form-control'}),
        #     'persons': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
        fields = '__all__'
