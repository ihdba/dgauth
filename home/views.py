from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Movies Store'
    ctx = {
        'title': title,
    }
    return render(request, 'home/index.html', ctx)





def about(request):
    
    title = 'About'
    ctx = {
        'title': title,
    }
    return render(request, 'home/about.html')