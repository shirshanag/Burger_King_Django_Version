from django.db import models

# Create your models here.
class Book_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField()
    mobile=models.CharField()
    date=models.CharField()
    time=models.CharField()
    guests=models.IntegerField()
    class Meta:
        db_table='Book_data'