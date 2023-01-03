from django.db import models

# Create your models here.

class user_signup(models.Model):
    name=models.CharField(max_length=30)
    adrs=models.TextField()
    city=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    pasword=models.CharField(max_length=50)

class add_book(models.Model):
    book_name=models.CharField(max_length=50)
    aurthor=models.CharField(max_length=50)
    add_date=models.DateTimeField()
    edition=models.CharField(max_length=20)

class contactus(models.Model):
    name=models.CharField(max_length=20)
    number=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=70)

class book_issue(models.Model):
    s_name=models.CharField(max_length=50)
    book_name=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    issue_date=models.DateField()
    submit_date=models.DateField()
    