from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Service(models.Model):
    Service_type = models.CharField(max_length=255)
    image = CloudinaryField('image')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Service_type
    

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=500)
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    linkedIn = models.URLField(max_length=300, blank=True, null=True)
    image = CloudinaryField('image')
    
    
    def __str__(self):
        return self.full_name
    


class Past_Paper(models.Model):
    STANDARD_CHOICES = [
        ('standard 1','standard 1'),
        ('standard 2','standard 2'),
        ('standard 3','standard 3'),
        ('standard 4','standard 4'),
        ('standard 5','standard 5'),
        ('standard 6','standard 6'),
        ('standard 7','standard 7')
    ]


    subject = models.CharField(max_length=300)
    description = models.TextField()
    year = models.PositiveIntegerField()
    image = CloudinaryField('image')
    standard = models.CharField(max_length=20,choices=STANDARD_CHOICES)
    pdf_file = CloudinaryField('image')
    time_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.year})- {self.standard}"



class Book_Category(models.Model):
    category = models.CharField(max_length=300)
    total_books = models.PositiveIntegerField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.category


class Register_Book(models.Model):
     book_name = models.CharField(max_length=500)
     price = models.IntegerField()
     class_level = models.CharField(max_length=255)
     available_book = models.IntegerField()
     date_uploaded = models.DateTimeField(auto_now_add=True)
     image = CloudinaryField('image')
     def __str__(self):
         return self.book_name
     
class Testimonial(models.Model):
    client_name = models.CharField(max_length=300)
    profession = models.CharField(max_length=300)
    discription = models.TextField()
    image = CloudinaryField('image')
    def __str__(self):
        return self.client_name




class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('books', 'Books'),
        ('lesson_plan', 'Lesson Plan'),
        ('schemes_of_work', 'Schemes of Work'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return self.category
    

class CustomerMessage(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.full_name
