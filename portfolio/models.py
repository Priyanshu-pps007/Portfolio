from django.db import models

class Userr(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=1000 , null=True,blank=True)

    def __str__(self):
        return self.name
    

# Create your models here.
