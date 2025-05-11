from django.shortcuts import render

# Create your views here.
def unchartedaction(request):
    return render(request, 'uncharted.html')