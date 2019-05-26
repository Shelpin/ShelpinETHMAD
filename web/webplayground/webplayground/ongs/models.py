from django.db import models

class Ong(models.Model):
    name = models.CharField(max_length=150)
    bank = models.IntegerField()

    def __str__(self):
        return self.name