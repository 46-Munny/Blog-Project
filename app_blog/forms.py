from django import forms
from app_blog.models import blog, comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=('comments',)
