from django.db import models

class receipe(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='receipe_images/')
