from django.contrib import admin

from .models import student,Image,Hi

class StudentInfoAdmin(admin.ModelAdmin):
	list_display = ('name',)

class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ('id','img',)

class HiInfoAdmin(admin.ModelAdmin):
	list_display = ('Hello',)

admin.site.register(student,StudentInfoAdmin)
admin.site.register(Image,ImageInfoAdmin)
admin.site.register(Hi,HiInfoAdmin)