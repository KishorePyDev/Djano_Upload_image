from django.db import models

# Create your models here.
# models.py 
class Upload(models.Model): 
	image = models.ImageField(null=True, blank=True, upload_to="pics/") 
