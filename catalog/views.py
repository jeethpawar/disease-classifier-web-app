from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.GET) 
    return render(request, "index.html")

