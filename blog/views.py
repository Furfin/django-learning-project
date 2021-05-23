from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import random
import datetime
from django.urls import reverse
from .models import Post,Comment
from users.forms import CommentCreationForm
from django.http import HttpResponseRedirect
# Create your views here.
headings=['Hey, its me Furfin','My name is Furfin']

def blog_home(request):
  
  context={
    'posts':Post.objects.order_by('date_posted')[::-1],
    'heading':headings[random.randint(0,len(headings)-1)]
  }

  return render(request, 'blog/blog_home.html', context)


def com_delete(request,*args, **kwargs):
  object = Comment.objects.get(id=kwargs['pk'])
  object.delete()

  return HttpResponseRedirect('http://127.0.0.1:8000/')

def about(request):
  return render(request, 'blog/about.html',{'title':'About','heading':headings[random.randint(0,len(headings)-1)]})

class PostListView(ListView):
  model = Post
  template_name = 'blog/blog_home.html'
  context_object_name = 'posts'
  queryset = Post.objects.order_by('-date_posted')[::-1]
  paginate_by = 4

  def get_queryset(self):
    fil = self.request.GET.get('filter', '')
    if fil=='':
      queryset = Post.objects.order_by('-date_posted')[::-1]
      return queryset
    else:
      try:
        fil = User.objects.filter(username = fil).first()
        fil = fil.id
        queryset = Post.objects.filter(author=fil)
        return queryset
      except:
        queryset = []
        return queryset

  def get_context_data(self, **kwargs):
    context = super(PostListView, self).get_context_data(**kwargs)
    context['filter'] = self.request.GET.get('filter', '')
    return context



class PostDetailView(DetailView):
  model = Post


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post=self.get_object()
    if self.request.user == post.author:
      return True
    else:
      return False

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Post
  fields = ['title','content']

  def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
  model = Post
  fields = ['title','content','image']

  def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    post=self.get_object()
    if self.request.user == post.author:
      return True
    else:
      return False



class CommentCreateView(CreateView):
  model = Comment
  form_class = CommentCreationForm
  template_name = 'blog/comment_form.html'
  success_url = '/'
  def form_valid(self,form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)
