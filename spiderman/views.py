from django.shortcuts import render

# Create your views here.
def spidermanaction(request):
    return render(request, 'spiderman.html')