from django.shortcuts import render
from listings.models import Band
from django.http import HttpResponse


def hello(request):
    bands = Band.objects.all()
    

    return render(request, 'bands/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')