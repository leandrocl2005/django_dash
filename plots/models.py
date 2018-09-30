from django.db import models
from django.utils import timezone

# Create your models here.
class Plot(models.Model):
	title = models.CharField(max_length=30)
	xlabel = models.CharField(max_length=30)
	ylabel = models.CharField(max_length=30)
	upload = models.FileField(upload_to='uploads/')

	def __str__(self):
		return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name