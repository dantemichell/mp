from django import forms
from .models import Mascota
from django.forms import ModelForm, DateInput, DateField
import datetime

class AdoptForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'fecNac',
			'raza',
            'imagen1',
            'sexo',
            'tamaño',
			'estado',
			'descripcion'

            ]
        widgets = {
			'fecNac': forms.SelectDateWidget(years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year)),
   
			}

		
class AdoptingForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [            
			'estado',			
            ]
        