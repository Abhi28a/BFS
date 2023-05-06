from django.db import models
# Create your models here.
class GoldLoan(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    mail=models.CharField(max_length=20)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    reqamount=models.IntegerField()
    annualincome=models.IntegerField()

    def __str__(self):
        return self.fname

class EduLoan(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    mail=models.CharField(max_length=20)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    reqamount=models.IntegerField()
    annualincome=models.IntegerField()

    def __str__(self):
        return self.fname

class HomeLoan(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    mail=models.CharField(max_length=20)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    reqamount=models.IntegerField()
    annualincome=models.IntegerField()

    def __str__(self):
        return self.fname

class PersonalLoan(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    street=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    mail=models.CharField(max_length=20)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    reqamount=models.IntegerField()
    annualincome=models.IntegerField()

    def __str__(self):
        return self.fname


class Uploaded_Documents(models.Model):
    username=models.CharField(max_length=30)
    aadhar=models.FileField()
    pan=models.FileField()

    def __str__(self):
        return self.username