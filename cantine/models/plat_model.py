from django.db import models
from .menu_model import Menu
class Plat(models.Model):
    id = models.OneToOneField(Menu, on_delete=models.CASCADE, primary_key=True, related_name='plat')
    name = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.name