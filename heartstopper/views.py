from django.shortcuts import render

# Create your views here.
def heartstopperaction(request):
    return render(request, 'heartstopper.html')