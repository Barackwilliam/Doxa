from django.contrib import admin
from .models import Teacher,Past_Paper, Service,Book_Category,Register_Book,Testimonial,Gallery,CustomerMessage
# Register your models here.

admin.site.register(Service)

@admin.register(Past_Paper)
class Past_PaperAdmin(admin.ModelAdmin):
    list_display = ('subject','description','year','standard','cover_image','pdf_file','time_uploaded')
    search_fields = ('subject','year','standard')
    list_filter = ('standard','year')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name','subject','facebook_link','twitter_link','linkedIn','image')
    search_fields = ('full_name','subject')
    list_filter = ('full_name','subject')

   
@admin.register(Book_Category)
class Book_CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','total_books','image')
    search_fields = ('category','total_books')
    list_filter = ('category','total_books')



@admin.register(Register_Book)
class Register_BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','price','class_level','available_book','date_uploaded','image')
    search_fields = ('book_name','price','class_level')
    list_filter = ('book_name','class_level','price')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name','profession','discription','image')
    search_fields = ('client_name','profession')
    list_filter = ('client_name','profession')





@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('category','image','description')
    search_fields = ('category','description')
    list_filter = ('category','image')



@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','subject','message')
    search_fields = ('full_name','email')
    list_filter = ('full_name','email')


