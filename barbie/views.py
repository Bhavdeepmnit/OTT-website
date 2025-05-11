from django.shortcuts import render

# Create your views here.
def barbieaction(request):
    return render(request, 'barbie.html')