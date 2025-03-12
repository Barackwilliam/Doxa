from django.contrib import admin
from .models import Electronic,Male_clothe,Female_clothe,Child_clothe,Testimonial,Handbag,Shoe,Brand,Message
# Register your models here.

admin.site.register(Brand)

@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','description','available_product','image1','image2')
    search_fields = ('product_name','price','available_product')
    list_filter = ('product_name','price')



@admin.register(Male_clothe)
class Male_clotheAdmin(admin.ModelAdmin):
    list_display = ('type_of_clothes','regular_price','old_price','description','image1','image2')
    search_fields = ('type_of_clothes','regular_price')
    list_filter = ('type_of_clothes','regular_price')


@admin.register(Female_clothe)
class Female_clotheAdmin(admin.ModelAdmin):
    list_display = ('type_of_clothes','regular_price','old_price','description','image1','image2')
    search_fields = ('type_of_clothes','regular_price')
    list_filter = ('type_of_clothes','regular_price')

@admin.register(Child_clothe)
class Child_clotheAdmin(admin.ModelAdmin):
    list_display = ('type_of_clothes','regular_price','old_price','description','image1','image2')
    search_fields = ('type_of_clothes','regular_price')
    list_filter = ('type_of_clothes','regular_price')



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name','description','image')
    search_fields = ('client_name','description')
    list_filter = ('client_name','description')

@admin.register(Handbag)
class HandbagAdmin(admin.ModelAdmin):
    list_display = ('type_of_bag','regular_price','old_price','description','image1','image2')
    search_fields = ('type_of_bag','regular_price')
    list_filter = ('type_of_bag','regular_price')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','subject','message','phone_number')
    search_fields = ('full_name','email','phone_number')
    list_filter = ('full_name','email')
