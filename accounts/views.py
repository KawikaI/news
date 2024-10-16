from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Corrected from 'from_class' to 'form_class'
    success_url = reverse_lazy('login')  # Redirect to the login page after successful sign-up
    template_name = "registration/signup.html"  # Path to the template for the sign-up page
    



# Create your views here.
