from django.db import models


class model_user(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=15)
    mail = models.EmailField()
    password = models.CharField(max_length=100)

class donor(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=5)
    contactno = models.IntegerField()
    mail = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    emergency = models.IntegerField()
    organtype = models.CharField(max_length=100)
    agreement = models.CharField(max_length=100)

STATUS = (('approved', 'Approved'),('rejected', 'Rejected'),('applied', 'Applied'), )
class Hospital(models.Model):
    h_name = models.CharField(max_length=20)
    own_name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    ph = models.IntegerField()
    email = models.EmailField()
    pswd = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS, default='applied')    
   
class recipient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=5)
    organ = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    mail = models.EmailField()
    address = models.CharField(max_length=100)

class feed(models.Model):
    name = models.CharField(max_length=15)
    phone = models.IntegerField()
    mail = models.EmailField()
    message = models.CharField(max_length=50)