from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .forms import  AddcontactForm,ContactUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Contact
from .views import HttpResponse

# Create your views here.



# class Home(View):
#     def get(self,request):
#         return render(request,'index.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Addcontact(View):
    def get(self, request):
        form = AddcontactForm()
        return render(request, 'addcontact.html', {'form': form})
    
    def post(self, request):
            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            Contact.objects.create(name=name,email=email,phone=phone)
            messages.success(request,'contact added succesfully')
            return redirect('home_view')
 

         
class ListContact(View):
    def get(self,request):
        todo=Contact.objects.all()
        return render(request,'view_contact.html',{'todo':todo})
       

class ContactDetailView(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("id")
          todo=Contact.objects.get(id=id)
          return render(request,'contact_detail.html',{'Contact':todo})
          

class ContactDeleteView(View):
     def get(self, request, *args, **kwargs):
          id=kwargs.get("id")
          todo=Contact.objects.get(id=id)
          todo.delete()
          messages.success(request,"contact deleted succesfully")
          return redirect("con_view")




class ContactUpdateView(View):
     def get(self, request, *args, **kwargs):
          id=kwargs.get("id")
          todo=Contact.objects.get(id=id)
          form=ContactUpdateForm(request.POST,instance=todo)

          return render(request,'con_update.html',{'form':form})
     
     def post(self,request,*args,**kwargs):
          id=kwargs.get("id")
          todo=Contact.objects.get(id=id)
          form=ContactUpdateForm(request.POST,instance=todo)
          messages.success(request,"contact updated successfully")

          if form.is_valid():
               form.save()
               return redirect("con_view")