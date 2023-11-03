from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 border rounded-xl'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image','condition')
        widgets = {

            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder':'Choose'
            }),
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                    
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'condition': forms.Select(attrs={
                'class': INPUT_CLASSES 
            }),
        }            
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold','condition')
        widgets = {   
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'condition': forms.Select(attrs={
                'class': INPUT_CLASSES 
            }),
        }            
            
                    
        

