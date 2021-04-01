from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'inventory/home.html')


def about(request):
    return render(request, 'inventory/about.html')

def billing(request):
    return render(request, 'inventory/billing.html')