from unicodedata import name
from django.shortcuts import render

def home_view(request): 
    return render(request, 'home.html')

def contact_view(request): 
    return render(request, 'contact.html')

def skills_view(request): 
    return render(request, 'skills.html')

def experience_view(request): 
    return render(request, 'experience.html')
