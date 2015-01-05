#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from django.template.response import TemplateResponse as TR
from django.template import RequestContext
from shixisheng.models import student,Image

#http返回值
def home(request):
	d = {"date":str(datetime.datetime.now())}

	all = student.objects.all()
	d['all'] = all

	all_image = Image.objects.all()
	d['all_img'] = all_image

	return TR(request,"index.html",d)

def hello(request,abcd):
	#return HttpResponse("hello world! I'm coming" + abcd)
	d = {'ab':abcd,"date":str(datetime.datetime.now())}
	all = student.objects.all()
	#all = student.object.filter(name = "jike")
	d['all'] = all

	return TR(request,"hello.html",d)
	return render_to_response("hello.html",d,context_instance=RequestContext(request))

def new(request):
	print request.POST
	s = student()
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.content = request.POST['content']
	s.content = 0
	s.save()
	
	return redirect("/hello/fdsa")

def delete(request,id):
	s = student.objects.get(id=int(id))
	#s = student.objects.get(name="jike") , 在整条记录中查找name为jike这条记录。
	s.delete()
	return redirect("/hello/fdsa")

def edit_view(request,id):
	s = student.objects.get(id=int(id))
	time = datetime.datetime.now()
	d = {"s":s,"t":str(time)}
	return TR(request,"edit.html",d)
	
def edit(request,id):
	s = student.objects.get(id=int(id))
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.save()
	return redirect("/hello/fdsa") 