from django.db import models

# Create your models here.
from enum import Enum


class CarType(models.Model):
  type = models.CharField(max_length=20, blank=False)
  def __str__(self) -> str:
     return self.type
  
class Cars(models.Model):
    type = models.OneToOneField(CarType,on_delete=models.CASCADE);
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20, blank=False)
    con = models.CharField(
        max_length=40,
        choices=[('se', 'Sedan'),('hat','hatch')],
        default= "",
    )

