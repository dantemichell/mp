from django.shortcuts import render , redirect
from .forms import AdoptForm

def adopt(request):
    if request.method =="POST":
        form = AdoptForm(request.POST)
        if form.is_valid():
            Mascota = form.save(commit=True)
            Mascota.save()
            return redirect('/admin/')
    else:
        form = AdoptForm()
    return render(request, '/templates/adoptar.html', {'form': form})
