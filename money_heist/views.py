from django.shortcuts import render

# Create your views here.
def heistaction(request):
    return render(request, 'money heist.html')