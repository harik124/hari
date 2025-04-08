from django.db import models
from admin_view.models import *
# Create your models here.
class USER_DB(models.Model):
    # Basic Information
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    
    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Address Information
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    # Terms Acceptance
    terms_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class bookTrip(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(USER_DB, on_delete=models.CASCADE)
    trip=models.ForeignKey(Trip, on_delete=models.CASCADE)
    guid=models.ForeignKey(TourGuide, on_delete=models.CASCADE ,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} "

class Review(models.Model):
    """Simple review model with just name and review content"""
    name =  models.ForeignKey(USER_DB, on_delete=models.CASCADE)
    review_title = models.TextField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"Review by {self.name} ({self.created_at.date()})"