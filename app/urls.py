from django.urls import path
from .views import home, test, allexamples, about
app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('test', test, name='test'),
]