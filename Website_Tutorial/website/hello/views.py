from django.shortcuts import render
from django.http import HttpResponse

name = [
    {'pogi': 'Scantlin',
     'matalino': 'Ricson',
     'maaasahan' : 'Marianne'},
    {'pogi': 'Bea',
     'matalino': 'Hazel', 
     'maaasahan' : 'Kiana'},
    {'pogi': 'Justin',
     'matalino': 'Mariel',
     'maaasahan': 'Kenneth'}
]

def home(request):
    six_G = {
        'name':name
    }
    return render(request, 'hello/home.html', six_G)

def index(request):
    return render(request, 'hello/about.html',  {'title':'About'})
