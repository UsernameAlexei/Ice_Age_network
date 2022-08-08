from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(attrs={'rows': 1, 'placeholder': 'Write your title here'}),
                            label="",
                            )

    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post here'}),
                           label="",
                           )

    class Meta:
        model = Posts
        fields = ('title', 'body')
        exclude = ("user",)




