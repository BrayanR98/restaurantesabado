from django import forms

class FormularioEmpleados(forms.Form):
    CARGO=(
        (1,'Cheff'),
        (2,'Administrador'),
        (3,'Mesero'),
        (4,'Ayudante')
    )
    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
        
    )
    salario = forms.CharField(
        required=True,
        max_length=11,
        widget= forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    direccion = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(attrs={'class' : 'form-control mb-3'})
        
    )
    telefono = forms.CharField(
        required=True,
        max_length=11,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
        
    )
    fotografia = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'form-control mb-3'})
        
    )
    
    tipoempleado = forms.ChoiceField(
        required=True,
        widget= forms.Select(attrs={'class' : 'form-select mb-3'}),
        choices=CARGO
    )