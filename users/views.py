from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user=form.save()
      username=form.cleaned_data.get('username')
      messages.success(request,f'Account created for {username}')
      user=authenticate(username=username,password=form.cleaned_data['password1'])
      login(request,user)
      return redirect('blog-home')

  else:
    form = UserRegisterForm()
  return render(request,'users/register.html', {'form': form})


@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,'Account updated')
      return redirect('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request,'users/profile.html',context)

class ProfileDetailView(DetailView):
  model = User
  template_name = 'users/profile_detail.html'