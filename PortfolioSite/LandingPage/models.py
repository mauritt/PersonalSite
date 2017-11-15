from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=25)
    heading = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
