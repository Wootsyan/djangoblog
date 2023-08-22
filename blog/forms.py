from django import forms
from .models import Post

class ImgForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']
        
class PostForm(forms.ModelForm):

    title = forms.CharField(help_text="Maksymalnie 200 znaków")
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']