from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.



class Electronic(models.Model):
    product_name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField()
    available_product = models.PositiveIntegerField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
   
    def __str__(self):
        return self.product_name




class Male_clothe(models.Model):
    type_of_clothes = models.CharField(max_length=300)
    regular_price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')


    def __str__(self):
        return self.type_of_clothes




class Female_clothe(models.Model):
    type_of_clothes = models.CharField(max_length=300)
    regular_price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')


    def __str__(self):
        return self.type_of_clothes




class Child_clothe(models.Model):
    type_of_clothes = models.CharField(max_length=300)
    regular_price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')

   

    def __str__(self):
        return self.type_of_clothes


    

     
class Testimonial(models.Model):
    client_name = models.CharField(max_length=300)
    description = models.TextField()
    image = CloudinaryField('image')

    #image = CloudinaryField('image')
    def __str__(self):
        return self.client_name




class Handbag(models.Model):
    type_of_bag = models.CharField(max_length=300)
    regular_price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')

   

    def __str__(self):
        return self.type_of_bag




class Shoe(models.Model):
    type_of_shoes = models.CharField(max_length=300)
    regular_price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField()
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
   

    def __str__(self):
        return self.type_of_shoes


class Brand(models.Model):
    brand_name = models.CharField(max_length=300)
    image = CloudinaryField('image')
    link = models.URLField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.brand_name




class Message(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name