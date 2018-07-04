from django.shortcuts import render
import random
from django.http import HttpResponse ,HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import FaveRest
from .form import RestcreateForm ,  RestEditForm , NewRestCreateForm

# Create your views here.

class HelloView(TemplateView):
	template_name = "say_hello.html"


class WelcomView(View):
	def get(self , request,*args , **kwargs):
		context = {}
		return render(request,"welcome.html",context)




class NewList(ListView):
	template_name="new_rest.html"
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug != "create":
			if slug != None :
				queryset=FaveRest.objects.filter(locat__iexact=slug)
			else:
				queryset=FaveRest.objects.all()
			return queryset
		else :
			create_some()


class DetailList(DetailView):
	template_name="rest_detail.html"
	queryset=FaveRest.objects.all()
	def get_context_data(self, **kwargs):
		context = super(DetailList,self).get_context_data( **kwargs)
		return context
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++		
#+ create methods +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def create_some(request) :
# 	form = RestcreateForm()
# 	context={"form" : form}
# 	temp = "form.html"
# 	if request.method == "POST":
# 		form = RestcreateForm(request.POST)
# 		if form.is_valid():			
# 			FaveRest.objects.create(
# 				name=form.cleaned_data.get("name"),
# 				locat = form.cleaned_data.get("locat")
# 			)
# 		return HttpResponseRedirect("/rest")
# 	return render(request,temp,context)

# def create_some(request) :
# 	form = NewRestCreateForm()
# 	context={"form" : form}
# 	temp = "form.html"
# 	if request.method == "POST":
# 		form = NewRestCreateForm(request.POST)
# 		if form.is_valid():			
# 			form.save()
# 		return HttpResponseRedirect("/rest")
# 	return render(request,temp,context)


class CreateRest(CreateView):
	template_name = "form.html"
	form_class = NewRestCreateForm
	success_url = "/rest/"

def edit_rest(request,**kwargs) :
	slug = kwargs.get("slug")
	obj = FaveRest.objects.get(slug=slug)
	form = RestEditForm(initial={'name': obj.name,
								 'locat' : obj.locat,
								 'email' : obj.email,
								 })
	context={"form" : form}
	temp = "edit_form.html"
	if request.method == "POST":
		form = RestEditForm(request.POST)
		if form.is_valid():			
			FaveRest.objects.filter(slug=slug).update(
				name=form.cleaned_data.get("name"),
				locat = form.cleaned_data.get("locat"),
				email = form.cleaned_data.get("email"),
				slug = form.cleaned_data.get("name")		
			)
		return HttpResponseRedirect("/rest")
	return render(request,temp,context)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class RemoveView(View):
	def get(self , request,*args , **kwargs):
		slug=kwargs.get("slug")
		FaveRest.objects.filter(slug=slug).delete()
		return HttpResponseRedirect("/rest")


		