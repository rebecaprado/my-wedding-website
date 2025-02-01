from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from decouple import config
from .forms import SitePassword
from .models import ConfirmationForm
from django.views.decorators.cache import never_cache


# Create your views here.


# To create a hashed password for the website, I got some help from ChatGPT.
# I hashed the password and saved it as an environment variable in the .env file.
# This allows me to use it locally without losing access, as the variable persists across sessions safely.
HASHED_PASSWORD = config("HASHED_PASSWORD") 


def index(request):
    error_message = None

    if request.method == "POST":
        # Save the user's input for the website's password as a form. To access the website, users must provide a password, 
        # which is the same for all invited guests
        form = SitePassword(request.POST)

        if form.is_valid():
            user_password = form.cleaned_data["password"]

            # Check if both passwords are equal. If so, redirect to the 'Home' Page
            if check_password(user_password, HASHED_PASSWORD):
                request.session['access'] = True
                return HttpResponseRedirect(reverse("home"))
            
            # Else, displays error message
            error_message = "Senha incorreta. Tente novamente."
        
        # If the user's password is None or empty, return error message
        else:
            error_message = "Insira uma senha válida."
        
    return render(request, 'website/index.html', {
        "error_message": error_message,
        "form": SitePassword()
    })


def home(request):
    # If a session has not been created (invalid password/attempt to access without password), redirect to the index page
    if not request.session.get('access'):
        return HttpResponseRedirect(reverse('index'))
    
    form = ConfirmationForm()
    return render(request, "website/home.html", {
        "form": form,
        "message": "",
        "message_type": ""
    })


@never_cache
def rsvp(request):
    form = ConfirmationForm()

    if request.method == "POST":
        form = ConfirmationForm(request.POST)

        if form.is_valid():

            # Save data collected from Django ModelForm
            instance = form.save()

            confirmation_status = form.cleaned_data['confirmation']
            if confirmation_status == 'no':
                instance.days_present.set([])

            return JsonResponse({"success": True, "message": "Resposta enviada com sucesso!"})
        
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
        
       