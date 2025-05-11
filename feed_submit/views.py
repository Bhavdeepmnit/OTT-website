from django.shortcuts import render

# Create your views here.
def feed_submitaction(request):
    return render(request, 'feed_submit.html')