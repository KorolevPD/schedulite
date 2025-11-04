from .views import RegisterView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path("registration/", RegisterView.as_view(), name="registration"),
]
