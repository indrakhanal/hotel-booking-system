
from django import forms
from.models import FillCostumerForm


class CostumerForm(forms.ModelForm):
    room_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    permanent_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    temporary_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_costumer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    relationship = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = FillCostumerForm
        exclude = ['c_id']