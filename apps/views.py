from django.shortcuts import render
from .forms import MyMessage

from .models import Electronic,Male_clothe,Female_clothe, Child_clothe,Testimonial,Shoe,Handbag,Brand


from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

import requests
from django.http import HttpResponse




# from .forms import MyMessage

# def contact(request):
#     ujumbe = ""

#     if request.method == 'POST':
#         form = MyMessage(request.POST)
#         if form.is_valid():
#             form.save()
#             ujumbe = "Hongera! Ujumbe wako umetumwa kikamilifu."
#             return redirect('contact')  # Kuzuia double submission
#     else:
#         form = MyMessage()

#     context = {
#         'form': form,
#         'ujumbe': ujumbe
#     }
#     return render(request, 'contact.html', context)



# Home Page
def home(request):
    #past_papers = Past_Paper.objects.all()[:3]
    electronics = Electronic.objects.all()
    female_clothes = Female_clothe.objects.all()
    testimonial = Testimonial.objects.all()
    child_clothes = Child_clothe.objects.all()
    male_clothes = Male_clothe.objects.all()
    brands = Brand.objects.all()


    
   
    context = {
       'electronics':electronics,
       'female_clothes':female_clothes,
       'testimonial':testimonial,
       'child_clothes':child_clothes,
       'male_clothes':male_clothes,
       'brands':brands
    }
 
    return render(request, 'index.html',context)


    


from .forms import MyMessage

def contact(request):
   brands = Brand.objects.all()
   ujumbe = ""

   if request.method == 'POST':
      form = MyMessage(request.POST)
      if form.is_valid():
         form.save()
         ujumbe = "Hongera! Ujumbe wako umetumwa kikamilifu."
         return redirect('contact')  # Kuzuia double submission
   else:
      form = MyMessage()

   context = {
        'form': form,
        'ujumbe': ujumbe,
        'brands':brands
   }
   return render(request, 'contact.html', context)




def female(request):
   brands = Brand.objects.all()
   female_clothes = Female_clothe.objects.all()
    
   context = {
       'female_clothes':female_clothes,
       'brands':brands
    }
 
   return render(request, 'female.html',context)




def electronic(request):
   brands = Brand.objects.all()
   electronics = Electronic.objects.all()
    
   context = {
       'electronics':electronics,
       'brands':brands
    }
 
   return render(request, 'electronic.html',context)



def male(request):
   brands = Brand.objects.all()
   male_clothes = Male_clothe.objects.all()
    
   context = {
       'male_clothes':male_clothes,
       'brands':brands
    }
 
   return render(request, 'male.html',context)

def child(request):
    child_clothes = Child_clothe.objects.all()
    brands = Brand.objects.all()
    
    context = {
       'child_clothes':child_clothes,
       'brands':brands
    }
 
    return render(request, 'child.html',context)


def shoes(request):
   brands = Brand.objects.all()
   sho = Shoe.objects.all()
    
   context = {
       'sho':sho,
       'brands':brands
    }
 
   return render(request, 'shoes.html',context)


def handbag(request):
   brands = Brand.objects.all()
   handbags = Handbag.objects.all()
    
   context = {
       'handbags':handbags,
       'brands':brands
    }
 
   return render(request, 'handbag.html',context)

