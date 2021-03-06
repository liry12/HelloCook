from django import forms
from .models import ArticleColumn
from .models import ArticlePost
from .models import Comment


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title", "abstract", "body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator", "body",)