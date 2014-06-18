from django.db import models


# Create your models here.

class Book(models.Model):
    book_text = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
class Author(models.Model):
    book = models.ForeignKey(Book)
    author_text = models.CharField(max_length=200)

class Total(models.Model):
    total = models.IntegerField(default=0) 


   
