from django import forms
from .models import Mascota

class AdoptForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'fecNac',
            'imagen1',
            'sexo',
            'tamaño',

            ]
        