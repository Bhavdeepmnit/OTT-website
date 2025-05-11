from django.shortcuts import render

# Create your views here.
def factoryaction(request):
    return render(request, 'kota factory.html')