from django.shortcuts import render, redirect
from .models import Station
from .forms import StationForm

def index(request):
    stations = Station.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'stations': stations})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = StationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
