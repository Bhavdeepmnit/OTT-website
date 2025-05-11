from django.shortcuts import render

# Create your views here.
def movieaction(request):
    return render(request, 'movies.html')