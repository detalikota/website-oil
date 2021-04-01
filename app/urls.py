from django.urls import path
from .views import home, test, allexamples
app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('test', test, name='test'),
    path('test2', allexamples, name='allexamples'),
]