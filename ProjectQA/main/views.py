from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def resume(request):
    return render(request, 'main/resume.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def contact(request):
    return render(request, 'main/contact.html')

