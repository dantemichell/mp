from django.shortcuts import render , redirect, get_object_or_404
from .forms import AdoptForm , AdoptingForm
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
    return render(request, 'templates/adoptform.html', {'form': form})

def galeria(request):
    mas = Mascota.objects.filter(estado='r').order_by('-nombre')
    return render(request, 'templates/galeria.html', {'posts': mas}) 

def gracias(request):
    return render(request, 'templates/gracias.html') 


def adoptar(request, id):
    perrito =  get_object_or_404(Mascota,id=id)
    form = AdoptingForm(request.POST or None, instance = perrito)
    if form.is_valid():
        x = form.save(commit=True)
        x.save()
        return redirect('gracias')
    else:
        form = AdoptingForm()
    return render(request, 'templates/perrito.html', {'form': form, 'perrito':perrito})
