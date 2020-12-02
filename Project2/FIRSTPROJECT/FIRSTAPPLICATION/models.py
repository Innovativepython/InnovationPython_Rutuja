from django.db import models

class students(models.Model):
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name



