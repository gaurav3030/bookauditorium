from django.db import models

# Create your models here.
class booking(models.Model):
    venue= models.CharField();
    event_name = models.CharField();
    date = models.DateField();
    time = models.Charfield();
    college = models.Charfield();
    email = models.EmailField();