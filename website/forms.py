from django import forms


# In order to create a Django Form for the website's password, it's necessary to create this class first
class SitePassword(forms.Form):
    password = forms.CharField(
        required=True, 
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'index-input-field', 'autocomplete': 'off'})
        )