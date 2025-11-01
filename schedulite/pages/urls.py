from django.urls import path
from django.views.generic import TemplateView, RedirectView


app_name = 'pages'

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/about.html'),
         name='index'),
    path('about/', RedirectView.as_view(pattern_name='pages:index',
                                        permanent=False)),
]
