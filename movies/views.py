from django.shortcuts import render

# Create your views here.

from .models import Movie

def index(request):
    
    title = 'Movies'
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
        
    #movies = Movie.objects.all()
    ctx = {
        'title': title,
        'movies': movies,
    }
    
    return render(request, 'movies/index.html', ctx)


def show(request, id):
    movie = Movie.objects.get(id=id)

    ctx = {
        'movie': movie,
    }
    
    return render(request, 'movies/show.html', ctx)