from django import forms

from .models import Post, Tag


class TagForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    keywords = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))

    class Meta:
        model = Tag
        exclude = ('user', )


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    keywords = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))

    class Meta:
        model = Post
        exclude = ('user', )
