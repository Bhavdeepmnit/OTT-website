from django.shortcuts import render

# Create your views here.
def oppenheimeraction(request):
    return render(request, 'oppenheimer.html')