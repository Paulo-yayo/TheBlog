from django.shortcuts import render




def about_podcast(request):
    return render(request, 'about_podcast.html', {})


def about_shop(request):
    return render(request, 'about_shop.html', {})


def about_media(request):
    return render(request, 'about_media.html', {})
    

def about_events(request):
    return render(request, 'about_events.html', {})


def term_conditions(request):
    return render(request, 'term_conditions.html', {})
