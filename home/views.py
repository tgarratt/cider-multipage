from django.shortcuts import render


def home(request):
    # returns homepage
    return render(request, "../templates/home.html")
