from django.shortcuts import render, HttpResponse

def index(request):
    context = {}
    return render(request, 'index.html', context)
