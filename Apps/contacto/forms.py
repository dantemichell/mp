from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'run',
            'nombre',
            'apellido',
            'correo',
            'fecha_nacimiento',
            'telefono',
            'region',
            'comuna',
            'tipovivienda',
            'mensaje',
            ]

        labels = {
            'run':'Rut',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'correo':'Correo',
            'fecha_nacimiento':'Fecha de nacimiento',
            'telefono': 'Telefono',
            'region': 'Region',
            'comuna': 'Comuna',
            'tipovivienda':'Tipo de vivienda',
            'mensaje':'Mensaje',
            }
        widgets = {
            'run': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'fecha_nacimiento': forms.SelectDateWidget(),
            'telefono': forms.TextInput(),
            'region': forms.TextInput(),
            'comuna': forms.TextInput(),
            'tipovivienda': forms.Select(),
            'mensaje': forms.Textarea(),        
            }
        
    def validarRut(self):
        rut = self.run
        rut = rut.upper()
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
        if str(res) != dv and dv!="K" and res!=10:
                raise forms.ValidationError("Rut inválido")
