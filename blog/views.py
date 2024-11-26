from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, 'blog/index.html')


def words(request):
    
    return render(request, 'blog/words.html')


def notes(request):
    
    return render(request, 'blog/notes.html')


def about(request):
    
    return render(request, 'blog/about.html')