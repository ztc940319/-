#coding:utf-8
from django.db import models

class Image(models.Model):#代表一个表
	img = models.ImageField(upload_to = './img') 


class student(models.Model):
	name    = models.CharField(max_length=30)
	address = models.CharField(max_length = 50)
	count   = models.IntegerField(default=0)
	date    = models.DateField(auto_now=True)
	content = models.TextField()

class Hi(models.Model):
	Hello    = models.CharField(max_length=30)

#class student1(models.Model):
	#name = models.CharField(max_length=30)
	#address = models.CharField(max_length = 50)