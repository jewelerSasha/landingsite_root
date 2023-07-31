from django.db import models

# Create your models here.
class Order(models.Model):
    order_dr = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=200)