from django.shortcuts import render , redirect, get_object_or_404
from .forms import AdoptForm
from . models import Mascota

def adopt(request):
    if request.method =="POST":
        form = AdoptForm(request.POST, request.FILES)
        if form.is_valid():
            Mascota = form.save(commit=True)
            Mascota.save()
            return redirect('/galeria/')
    else:
        form = AdoptForm()
    return render(request, 'templates/adoptar.html', {'form': form})

def galeria(request):
    mas = Mascota.objects.filter(estado='r').order_by('-nombre')
    return render(request, 'templates/galeria.html', {'posts': mas} 


def adoptar(request):
    return render(request, 'templates/galeria.htm',{})