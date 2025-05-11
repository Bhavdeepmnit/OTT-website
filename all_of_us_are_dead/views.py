from django.shortcuts import render

# Create your views here.
def deadaction(request):
    return render(request, 'all of us are dead.html')