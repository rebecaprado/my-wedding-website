from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

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
    days_present = models.ManyToManyField(DaysPresent, blank=True)
    date_of_confirmation = models.DateField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)


class CheckboxTextWidget(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        checkbox_html = super().render(name, value, attrs, renderer)

        return mark_safe(f"{checkbox_html}")


class ConfirmationForm(ModelForm):
    class Meta:
        model = GuestConfirmation
        fields = ['guest_name', 'confirmation', 'days_present', 'message']
        widgets = {
            'guest_name': forms.TextInput(attrs={'class': 'rsvp-form-field-name', 'autocomplete': 'off'}),
            'days_present': CheckboxTextWidget(),
            'message': forms.Textarea(attrs={'class': 'rsvp-form-field-message'})
        }
        labels = {
            'guest_name': 'Nome completo',
            'confirmation': 'Você irá aos eventos?',
            'days_present': 'Confirme qual(is) dia(s)',
            'message': 'Mensagem para os noivos'
        }