from django.shortcuts import render
# from firstORM_APP.models import Movie

# def index(request):
#     context = {
#        'all_movies' : Movie.objects.all()
#     }
#     return render(request, 'index.html', context)

# other imports
# from firstORM_APP import models
# from models import Movie
from .models import Movie
# show all of the data from a table
def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)