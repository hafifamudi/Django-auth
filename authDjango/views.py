from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import UserProfileInfoForm
from .models import UserProfileInfo

class IndexView(View):
    template_name = 'authDjango/index.html'

    def get(self,request):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'authDjango/register.html'

    def get(self,request):
        # create instance of form
        profile_form = UserProfileInfoForm()

        return render(request, self.template_name, {
            'profile_form':profile_form
        })

class RegisterUserView(View):
    
    def post(self,request):
        if request.POST['password'] == request.POST['password_validation']:
            profile_form = UserProfileInfoForm(request.POST,request.FILES)
            user_profile = UserProfileInfo()
            # cek if user exist or not
            user_exist = User.objects.filter(username=request.POST['username'])
            if user_exist:
                messages.success(request, 'user was exist, please register with different credentials!')
                return HttpResponseRedirect(reverse('authDjango:register'))

            # cek if the data valid or not
            elif profile_form.is_valid():
                username = profile_form.cleaned_data['username']
                email = profile_form.cleaned_data['email']
                password = profile_form.cleaned_data['password']

                # create and save user instance
                user = User.objects.create_user(username=username,password=password)
                user.save()
                
                # set the user data in profile_form so the profile_form not override data in user object
                user_profile.user = user
                user_profile.first_name =  profile_form.cleaned_data['first_name']
                user_profile.last_name = profile_form.cleaned_data['last_name']
                user_profile.email = profile_form.cleaned_data['email']
                user_profile.portfolio_site = profile_form.cleaned_data['portfolio_site']
                

                if 'profile_pic' in request.FILES:
                    user_profile.profile_pic = request.FILES['profile_pic']
                
                
                user_profile.save()
                
                messages.success(request, 'register succesfully!')
                return HttpResponseRedirect(reverse('authDjango:register'))

        else:
            messages.error(request, 'Password is not Matching!')
            return HttpResponseRedirect(reverse('authDjango:register'))
    
        return HttpResponseRedirect(reverse('authDjango:register'))
