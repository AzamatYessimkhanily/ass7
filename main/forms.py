from django import forms
from .models import Clothing,Shoes,Аccessories

class ClothingFilterForm(forms.Form):
    
    clothing_type = forms.MultipleChoiceField(choices=Clothing.CLOTHING_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    size = forms.MultipleChoiceField(choices=Clothing.SIZE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    color = forms.MultipleChoiceField(choices=Clothing.COLOR_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)


class ShoesFilterForm(forms.Form):
    
    shoe_type = forms.MultipleChoiceField(choices=Shoes.SHOE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    size = forms.MultipleChoiceField(choices=Shoes.SIZE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    color = forms.MultipleChoiceField(choices=Shoes.COLOR_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)


class AccessFilterForm(forms.Form):
    
    access_type = forms.MultipleChoiceField(choices=Аccessories.АCCESS_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    color = forms.MultipleChoiceField(choices=Аccessories.COLOR_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)

