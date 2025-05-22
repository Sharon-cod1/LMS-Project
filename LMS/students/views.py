from django.shortcuts import render

from django.views import View


class StudentRegisterView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'students/student-register.html')

