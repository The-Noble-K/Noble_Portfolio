from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=120)
    image = models.FilePathField(path="/img")

