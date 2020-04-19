from django.shortcuts import render, redirect, reverse


def home(request):
    # returns homepage
    return render(request, "../templates/home.html")
