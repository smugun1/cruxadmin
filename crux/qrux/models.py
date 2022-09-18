from django.db import models


# Create your models here.


class Farm_items(models.Model):
    datetime = models.DateField(default=None)
    f_items = models.CharField(max_length=200, default=None)
    f_quantity = models.IntegerField(default=None)
    f_total = models.IntegerField(default=None)

    def __str__(self):
        return str(self.datetime)


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name + "-" + self.email + ":" + self.phone

