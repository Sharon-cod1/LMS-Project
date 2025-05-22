from django.shortcuts import render,redirect

from django.views import View 

from .forms import LoginForm

from django.contrib.auth import authenticate,login,logout

class LoginView(View):
    
    def get(self,request,*args,**kwargs):
        
        form =LoginForm()
        
        data = {'page' : 'login-page','form':form}
        
        return render(request,'authentication/login.html',context=data)
   
    def post(self,request,*args,**kwargs):
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            
            if user :
                
                login(request,user)
            
            print(username,password)
            
            return redirect('home')
        
class LogoutView(View):

    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        return redirect('course_list')
        