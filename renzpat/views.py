from django.shortcuts import render
def home (request) : 
    return render(request, 'wedding_home.html')