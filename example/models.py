from django.db import models

class TestModel(models.Model):
    about = models.TextField(verbose_name="Text")


