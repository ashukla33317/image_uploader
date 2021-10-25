from django.shortcuts import render,redirect
from django.views import View
from .forms import ImageForm
from .models import Image
# Create your views here.

# def Home(request):
#     if request.method=='POST':
#         input_form=Image(photo=request.FILES['upload_image'])
#         input_form.save()
#     # form=ImageForm()
#     img=Image.objects.all()
#     return render(request,'index.html',{'img':img})

class Home(View):
    def get(self,request):
        img=Image.objects.all()
        return render(request,'index.html',{'img':img})
    
    def post(self,request):
        input_form=Image(photo=request.FILES['upload_image'])
        input_form.save()
        return redirect('/')
