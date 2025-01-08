from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    available_copies = models.IntegerField()
    
class UserTbl(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserTbl, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()
    overdue = models.BooleanField(default=False)
    

class Fine(models.Model):
    user = models.ForeignKey(UserTbl, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    paid = models.BooleanField(default=False)