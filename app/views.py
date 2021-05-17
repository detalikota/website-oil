from django.shortcuts import render

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

