from django.db import models

# Create your models here.
class Billing_Master(models.Model):
    Bill_Id = models.CharField(primary_key=True, max_length=50)
    S_No = models.IntegerField()
    Title = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Years = models.IntegerField(null=True)
    Months = models.IntegerField(null=True)
    Days = models.IntegerField(null=True)
    Gender = models.CharField(max_length=15)
    Phone = models.BigIntegerField()
    Alt_Phone = models.BigIntegerField()
    Email = models.EmailField(max_length=254)
    Refered_By = models.CharField( max_length=50)
    Address = models.CharField( max_length=50)
    Discount = models.FloatField()
    Final_Amount = models.FloatField(default=0)
    Advance = models.FloatField()
    Amount = models.FloatField()
    Date =  models.CharField(null=True, max_length=50)

class Billing_Details(models.Model):
    Bill_Id = models.ForeignKey("hospitalApp.Billing_Master", on_delete=models.CASCADE)
    Particulars = models.CharField( max_length=50)
    Price = models.FloatField()
    Date = models.CharField(null=True, max_length=50)


class Test_Master(models.Model):
    S_No = models.IntegerField()
    Test_Id = models.CharField(primary_key=True, max_length=50)
    Test_Name = models.CharField( max_length=50)
    Price = models.FloatField()