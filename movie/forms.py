from django import forms

from movie.models import MovieComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment 
        fields = ('content',)