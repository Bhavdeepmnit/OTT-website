from django.shortcuts import render

# Create your views here.
def blueaction(request):
    return render(request, 'red white and royal blue.html')