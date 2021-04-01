from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    brownie_points = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return render(self.firstname)