from django.forms import ModelForm,TextInput,Textarea,CheckboxInput
from .models import *



class AddForm(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'


        widgets = {
            'title': TextInput(attrs={'class':'title','name':'title','placeholder':'Title'}),
            'desc': Textarea(attrs={'class':'desc','name':'desc','placeholder':'Description'}),
            'complate': CheckboxInput(attrs={'class':'complate','name':'complate'}),
        }