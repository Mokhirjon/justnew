from django.db import models

# Create your models here.
class Twerk(models.Model):
    twerk_name=models.CharField(default='',max_length=13)
    twerk_birth=models.DateField()
    twerk_numb=models.CharField(max_length=31,default="")
    def __str__(self):
        return self.twerk_name