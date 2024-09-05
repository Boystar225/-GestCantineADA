from django import forms
from .models import Plat
from .models import Menu

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['name', 'summary']



class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['creation_date']
