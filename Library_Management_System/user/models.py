from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)
    num_available = models.PositiveIntegerField(default=1)
    

class BorrowedBook(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,null=True,blank=True,on_delete=models.CASCADE)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    
class Fine(models.Model):
     user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
     book = models.ForeignKey(Book,null=True,blank=True,on_delete=models.CASCADE)
     amount = models.DecimalField(max_digits=8,decimal_places=2)
     paid = models.BooleanField(default = False)
     
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

     
