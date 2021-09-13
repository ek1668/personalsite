from django.db import models
from datetime import datetime, date

# Create your models here.
class Personal(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phonenumber = models.CharField(max_length=50)
  title = models.CharField(max_length=50, null=True)
  about = models.TextField(blank=True, null=True)

class Experience(models.Model):
  position = models.CharField(max_length=50)
  company = models.CharField(max_length=50, default="compay")
  fromdate = models.DateTimeField(default=datetime.now, blank=True)
  todate = models.DateTimeField(default=datetime.now, blank=True)
  present = models.BooleanField(default=False)
  description = models.TextField(max_length=1000000, blank=True, null=True)

class Education(models.Model):
  university = models.CharField(max_length=50)
  degree = models.CharField(max_length=50)
  field = models.CharField(max_length=50)
  graduation = models.DateTimeField(default=datetime.now, blank=True)

class Skill(models.Model):
  workflow_skill = models.CharField(max_length=50)

class Certification(models.Model):
  issuer = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  dateissued = models.DateTimeField(default=datetime.now, blank=True)

class Photo(models.Model):
  img = models.ImageField(upload_to='pics/')
  
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=1000000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  
  

 