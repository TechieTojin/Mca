from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render("this is about us page")
