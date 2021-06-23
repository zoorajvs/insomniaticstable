from django import forms
from blog.models import Comment1


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ('name','body')

        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

