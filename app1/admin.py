from django.contrib import admin
from django.contrib.admin.decorators import display, register
from .models import Image
# Register your models here.

@admin . register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display=['id','photo','date']