from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
  
  
    def __str__(self):
        return self.name  
