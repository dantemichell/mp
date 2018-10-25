from django.shortcuts import render , redirect
from .forms import ContactForm

def contacto(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contacto = form.save(commit=True)
            Contacto.save()
            return redirect('/admin/')
    else:
        form = ContactForm()
    return render(request, 'templates/contacto.html', {'form': form})

	
def index(request):
    return render(request, 'templates/index.html', {})
