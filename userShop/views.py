from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class UserView(LoginRequiredMixin,View):
    login_url = '/auth/login'
    redirect_field_name ='/auth/login'
    
    template_name = 'userShop/index.html'


    def get(self,request):
        return render(request,self.template_name)