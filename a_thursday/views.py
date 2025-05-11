from django.shortcuts import render

# Create your views here.
def thursdayaction(request):
    return render(request, 'a thursday.html')