from django.shortcuts import render
from .forms import ContactForm

def contacto(request):
	form = ContactForm()
	return render(request, 'templates/contacto.html', {'form': form})
	
def index(request):
    return render(request, 'templates/index.html', {})
