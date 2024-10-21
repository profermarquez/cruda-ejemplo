from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['pais', 'forma_venta', 'forma_pago', 'producto', 'vendedor', 'fecha', 'ventas', 'cantidad', 'comision']
fecha = forms.DateField(input_formats=['%d-%m-%Y'])
