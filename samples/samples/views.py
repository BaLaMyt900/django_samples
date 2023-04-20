from django.shortcuts import render


def about_page(request):
    return render(request, 'about.html')


def index_page(request):
    return render(request, 'index.html')
