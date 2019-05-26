from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    donation = models.IntegerField()


    def __str__(self):
        return self.name