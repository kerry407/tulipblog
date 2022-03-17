from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import Profile
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=40)
    icon = models.CharField(max_length=20, default='icon')
    slug = models.SlugField(default=title)
   
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})




class Post(models.Model):   
    CATS = (
        ('Food', 'Food'),
        ('Business', 'Business'),
        ('Health & Fitness', 'Health & Fitness'),
        ('Travel', 'Travel')
    )
        
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )

   
    title = models.CharField(max_length=100)
    pre_content = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField(null=True,blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_posted = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author_pofiles = models.OneToOneField(Profile, on_delete=models.CASCADE, default=1)
    status = models.IntegerField(choices=STATUS, default=1)
    latest = models.BooleanField(null=True, blank=True, default=True)
    recent = models.BooleanField(null=True, blank=True, default=False)
    popular = models.BooleanField(null=True, blank=True, default=False)
    category = models.CharField(max_length=100, choices=CATS)
  

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name  = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextUploadingField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'Comment: {self.body} by {self.name}'

        

 
class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    message = RichTextUploadingField(null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30,choices=STATUS, default='New')

    def __str__(self):
        return self.full_name

class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'message']

class About(models.Model):
    about = models.TextField()
    