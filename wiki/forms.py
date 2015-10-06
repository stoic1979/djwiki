from django import forms

from models import Category, Article, Edit

class CategoryForm(forms.Form):
  title = forms.CharField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'slug']


class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        fields = ['summary']
