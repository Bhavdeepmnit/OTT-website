from django.shortcuts import render

# Create your views here.
def contactaction(request):
    return render(request, 'contact.html')