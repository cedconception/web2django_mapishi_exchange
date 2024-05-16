from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image', 'pub_date', 'is_published']

        # Optionally, you can customize the widgets if you want more control over the HTML
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}),
        }