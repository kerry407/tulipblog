from django import forms
from .models import *




class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ['name', 'email','body']


# choices = [('Food', 'Food'),('Travel', 'Travel'),('Business','Business'),('Health & Fitness','Health & Fitness')]
choices = Category.objects.all().values_list('title','title')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
   

    class Meta:
        model = Post
        fields = ['title','image', 'category','content']

        # widgets = {
        #     'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
        # }


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['full_name','email']