from django import forms
from .models import CreateBlog

class ArticleForm(forms.ModelForm):
    class Meta:
        model= CreateBlog
        fields = ['title', 'category', 'auteur', 'intro', 'body', 'image']
        labels = {'title': 'Titre', 'category': 'category', 'auteur': 'auteur',
                  'intro': 'introduction', 'body': 'description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','rows':5})
            
        }        