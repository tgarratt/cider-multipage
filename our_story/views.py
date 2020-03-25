from django.shortcuts import render


def our_story(request):
    # returns homepage
    return render(request, "../templates/our_story.html")
