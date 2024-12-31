from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.

class DaysPresent(models.Model):
    days_attending = models.CharField(max_length=20)

    def __str__(self):
        return self.days_attending


class GuestConfirmation(models.Model):
    CONFIRMATION_CHOICES = [
        ('yes', 'Sim'),
        ('no', 'Não')
    ]

    guest_name = models.CharField(max_length=150)
    confirmation = models.CharField(max_length=5, choices=CONFIRMATION_CHOICES)
    days_present = models.ManyToManyField(DaysPresent)
    date_of_confirmation = models.DateField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

class ConfirmationForm(ModelForm):
    class Meta:
        model = GuestConfirmation
        fields = ['guest_name', 'confirmation', 'days_present', 'message']
        widgets = {
            'days_present': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'guest_name': 'Nome',
            'confirmation': 'Confirme se irá ou não',
            'days_present': 'Caso vá, confirme qual(is) dia(s)',
            'message': 'Mensagem para os noivos'
        }