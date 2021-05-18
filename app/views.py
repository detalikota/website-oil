from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Service

def home(request):
    return render(request, 'app/home.html')
def about(request):
    return render(request, 'app/about.html')
def serviceburenie(request):
    return render(request, 'app/service-burenie.html')
def servicesverlenie(request):
    return render(request, 'app/service-sverlenie.html')
def contact(request):
    return render(request, 'app/contact.html')
def ourwork(request):
    return render(request, 'app/ourwork.html') 
class SearchResultsView(ListView):
    model = Service
    template_name = 'app/search.html'

    def get_queryset(self):
        return Service.objects.filter(
            name__icontains='е'
        ) .exclude(
            name__icontains='Сверление'
        )

