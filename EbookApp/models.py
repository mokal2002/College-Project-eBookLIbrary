from django.db import models
from datetime import time
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    book_id=models.AutoField
    name=models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    desc= models.TextField(max_length=1000)
    image = models.ImageField(upload_to="EbookApp/images" , default="")
    pdf_file = models.FileField(upload_to='ebooks/', default="")
    date = models.DateField(default="")
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Request(models.Model):
    rq_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name