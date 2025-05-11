from django.shortcuts import render

# Create your views here.
def aboutaction(request):
    return render(request, 'about.html')