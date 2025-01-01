from django import forms
from .models import Post, Poll, Choice


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)
