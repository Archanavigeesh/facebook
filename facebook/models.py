from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=260)
    password=models.CharField(max_length=20)
class Users(models.Model):
    user_id=models.ForeignKey(Login,on_delete=models.CASCADE)
    f_name=models.CharField(max_length=20)
    s_name=models.CharField(max_length=20)
    dob=models.DateField()
    gender=models.CharField(max_length=10)

