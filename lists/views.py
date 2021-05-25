from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# iterations we went thru (by adding the smallest amt of code to make it work)
# each of these, obviously failed and we tried to fix them.

# home_page = None

# def home_page()
#   pass

# def home_page (request):
#   pass

# def home_page (request):
#     return HttpResponse()

# def home_page (request):
#     return HttpResponse('<html>>')

# def home_page (request):
#     return HttpResponse('<html><title>To-Do Lists</title>')

def home_page(request):
    return render(request, 'home.html')

