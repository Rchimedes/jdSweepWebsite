from django.db import models


class Quote(models.Model):
    description = models.CharField(max_length=255)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length= 20)
    email = models.EmailField(max_length = 55)
    location = models.CharField(max_length = 255)
    custcategory = models.CharField(max_length=55)
    truckcategory = models.CharField(max_length=55)
    prevailing = models.CharField(max_length=55)
    hours = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length= 20)
    email = models.EmailField(max_length = 55)
    location = models.CharField(max_length = 255)
    interestedIn = models.CharField(max_length = 40)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
