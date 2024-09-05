from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField()

    def __str__(self):
        return f"Menu {self.id}"
