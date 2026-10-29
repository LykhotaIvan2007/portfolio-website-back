from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True)
    tools = models.CharField(max_length=255,  blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)


class Documents(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    year = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    thema = models.CharField(max_length=255, blank=True, null=True)
    doc = models.FileField(upload_to='docs', blank=True, null=True)