from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20,null = True,blank = True)
    last_name = models.TextField(max_length=20,null = True,blank = True)
    birth = models.DateField(max_length=20,null = True,blank = True)
    mobile_number = models.IntegerField(max_length=20,null = True,blank = True)
    GENDER_TYPE = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    gender = models.IntegerField(
        choices=GENDER_TYPE,
        default=1
    )
    def __str__(self):
        return str(self.street_name)

class Orders(models.Model):
    order_name = models.CharField(max_length=20,null = True,blank = True)
    order_price = models.IntegerField(max_length=20,null = True,blank = True)
    order_discount = models.IntegerField(max_length=20,null = True,blank = True)
    order_quantity = models.IntegerField(max_length=20,null = True,blank = True)
    order_address = models.TextField(max_length=20,null = True,blank = True)
    order_place_at = models.DateField(max_length=20,null = True,blank = True)


    
class StudentsAddress(models.Model):
    Student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    street_name = models.CharField(max_length=60,null = True,blank = True)
    house_no = models.IntegerField(max_length=60,null = True,blank = True)
    city = models.CharField(max_length=60,null = True,blank = True)
    state = models.CharField(max_length=60,null = True,blank = True)
    country = models.CharField(max_length=60,null = True,blank = True)
    pincode = models.CharField(max_length=60,null = True,blank = True)

    def __str__(self):
        return str(self.street_name)
    
