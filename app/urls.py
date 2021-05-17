from django.urls import path
from .views import home, about, serviceburenie, servicesverlenie, contact, ourwork
app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('ourwork', ourwork, name='ourwork'),
    path('service-burenie', serviceburenie, name='service-burenie'),
    path('service-sverlenie', servicesverlenie, name='service-sverlenie'),
]