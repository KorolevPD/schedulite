from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'),
         name='homepage'),
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
