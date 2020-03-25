from django.shortcuts import render

def contact_us(request):
    # returns homepage
    return render(request, "../templates/contact_us.html")
