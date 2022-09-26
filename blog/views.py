from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Category, Post, ContactForm, About, Subscribe
from .forms import CommentForm, PostForm, SubscribeForm
from django.core.paginator import Paginator 
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages  
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from users.models import User, Profile



# Create your views here.
def home(request):
    post = Post.objects.all()
    post1 = Post.objects.filter(latest=True).order_by('-date_posted')
    post3 = Post.objects.filter(recent=True)    
    post4 = Post.objects.filter(category='Travel')
    post5 = Post.objects.get(pk=18)
    bus = Post.objects.get(pk=19)
    travel = Post.objects.get(pk=23)
    health = Post.objects.get(pk=20)
    food = Post.objects.get(pk=18)
    post6 = Post.objects.get(pk=23)
    post7 = Post.objects.get(pk=20)
    post8 = Post.objects.filter(popular=True).order_by('-date_posted')[:4]
    post9 = Post.objects.filter(recent=True).order_by('-date_posted')[:3]
    
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            name = subscribe_form.cleaned_data.get('full_name')
            subscribe_email = subscribe_form.cleaned_data.get('email')
            subject = 'Thanks for subscribing to our blog!'
            message = 'Hi' + name + 'welcome to Tulip blog! We are very pleased to welcome you to our home. Thank you for also subscribing. We will keep you updated on our latest blogs.'
            try:
                email = send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[subscribe_email]
                )
                email.send(fail_silently=False)
            except Exception:
                messages.error(request,'We are having troubles connecting to our email server, this will be corrected as soon as posiible!')
            else: 
                messages.success(request, f'Thank you for subscribing {name}, we have sent an email to you!')
            return redirect('blog-home')
    else:
        subscribe_form = SubscribeForm()
    
    context = {
        'post': post,
        'post1': post1,
        'post3': post3,
        'post4': post4,
        'post5': post5,
        'post6': post6,
        'post7': post7,
        'post8': post8,
        'post9': post9,
        'food': food,
        'bus': bus,
        'travel': travel,
        'health': health,
        'subscribe_form': subscribe_form,
    }
    return render(request, 'blog/index.html', context)



def blog(request, pk):
    
    blog_post = Post.objects.get(id=pk)
    author = blog_post.author
    comments = blog_post.comments.filter(active=True)
    new_comment = None
    #comment posted

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post  = blog_post
            # Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'author': author,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    about = About.objects.get(pk=1)
    return render(request, 'blog/about.html', {'about': about})

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, f'Your message has been delivered Successfully, we will get back to you sooner or later!')
            return redirect('blog-contact')
    else:
        contact_form = ContactForm()
    
    context = {
        'contact_form': contact_form
    }
    return render(request, 'blog/contact.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/create_post.html'
    context_object_name = ''
    fields =['title','image', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def category(request, cats):
    category_post = Post.objects.filter(category=cats)
    category_name = Post.objects.filter(category=cats)[:1]
    paginator = Paginator(category_post,3)
    page= request.GET.get('page')
    paged_category = paginator.get_page(page)
    
    
    

    context ={
        'cats': cats,
        'category_post': paged_category,
        'category_name': category_name
    }
    return render(request, 'blog/blog_category.html', context)

