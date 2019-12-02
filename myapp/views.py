from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone


# Create your views here.
def home(request):
    post = Post.objects
    return render(request, 'home.html', {'post':post})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.date = timezone.datetime.now()
    new_post.body = request.POST['body']
    new_post.writer = request.POST['writer']
    new_post.save()
    return redirect('/myapp/' + str(new_post.id))

def edit(request, post_id):
    edit_post = Post.objects.get(id = post_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, post_id):
    update_post = Post.objects.get(id = post_id)
    update_post.title = request.POST['title']
    update_post.date = timezone.datetime.now()
    update_post.body = request.POST['body']
    update_post.writer = request.POST['writer']
    update_post.save()
    return redirect('/myapp/' + str(post_id))

def delete(request, post_id):
    delete_post = Post.objects.get(id = post_id)
    delete_post.delete()
    return redirect('home')

