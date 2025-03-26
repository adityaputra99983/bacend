from django.forms import ModelForm
from dasboart.models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta : 
        model=Barang
        fields='__all__'

        wigets = {
            'kodbrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'from-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }