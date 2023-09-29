from django.db import models

# Create your models here.

class profile(models.Model):
    name= models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.PositiveIntegerField()
    number=models.TextField(max_length=15)
    address=models.TextField(max_length=200)
    image = models.ImageField(upload_to='prof_image/' ,default="def.png")
    blood_group = models.CharField(max_length=3,null=True, blank=True)
    nationality=models.CharField(max_length=15)
    gender=models.CharField(max_length=9,null=True, blank=True)
    relegion =models.CharField( max_length=7,null=True, blank=True)
    qualification=models.CharField(max_length=15)
    date_of_birth=models.CharField(max_length=15)
    father_name=models.CharField(max_length=15)
    mother_name=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name