from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,postform
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.conf import settings
import random
from .models import post_model
# Create your views here.

#########.........employee info(home page).....
# @login_required
def employee(request):
    links=  User.objects.all().order_by('-date_joined')
    return render(request,'employee.html',{'links':links})

#.........post page ..................
@login_required
def post_page(request):
    links=  post_model.objects.all().order_by('-created_at')
    return render(request,'post_page.html',{'links':links})

#................CREATE  LINK.......................
@login_required
def link_create(request):
   if request.method== "POST":
     form = postform(request.POST, request.FILES)
     #ATA SAVE KORAR METHOD 
     if form.is_valid():
        link = form.save(commit=False)  
        link.user = request.user       
        link.save()
        return redirect('post_page')
   
   else:
      form = postform()
   return render(request, 'post_form.html' ,{'form': form})


#######################  ....EDIT FINCTION...........................
@login_required
def link_edit(request,link_id):
   links= get_object_or_404(post_model ,pk=link_id, user=request.user)

   if request.method == 'POST':
     form = postform(request.POST, request.FILES, instance= links)

     if form.is_valid():
        links = form.save(commit=False)  
        links.user = request.user       
        links.save()
        return redirect('post_page') 
      
   else:
      form = postform(instance=links)
   return render(request, 'post_form.html' ,{'form': form})

#############............DELETE LINK....................
@login_required
def link_delete(request,link_id):
  links= get_object_or_404(post_model, pk=link_id, user=request.user)

  if request.method=='POST':
     links.delete()
     return redirect('employee')  
  return render(request, 'link_confirm_deletion.html' ,{'post_model': post_model})

#..........registration.......
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('employee')
        else:
               print(form.errors) 
               return render(request, 'registration/register.html', {'form': form})


    else:
        form = UserRegistrationForm()

        return render(request, 'registration/register.html' ,{'form': form}) 
        

########...................check otp.....................................................................
