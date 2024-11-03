from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    format = models.CharField(max_length=30)
    file = models.FileField(upload_to='storage')

    class Meta:
        verbose_name_plural = "Media"