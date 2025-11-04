from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/registration_form.html"
    success_url = reverse_lazy("homepage")
