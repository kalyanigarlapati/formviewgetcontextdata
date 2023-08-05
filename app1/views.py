from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from typing import Any,Dict
from app1.forms import *


# Create your views here.
class Templatedata(TemplateView):
    template_name='Templatedata.html'
    
    
    def get_context_data(self,**kwargs):
        ecdo=super().get_context_data(**kwargs)
        ecdo['name']='kala'
        return ecdo



class insertdata(TemplateView):
    template_name='insertdata.html'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ecdo=super().get_context_data(**kwargs)
        sfo=studentForm()
        ecdo['sfo']=sfo
        return ecdo
    


    def post(self,request):
        sfd=studentForm(request.POST)
        if sfd.is_valid():
            sfd.save()
            return HttpResponse('data inserted')



class student(FormView):
    template_name='student.html'
    form_class=studentForm

    def form_valid(self, form:Any):
        form.save()
        return HttpResponse('student')
        #return super().form_valid(form)

    

    
    


