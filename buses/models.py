from django.db import models

# Create your models here.

class Bus(models.Model):
    reg_number = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.reg_number
