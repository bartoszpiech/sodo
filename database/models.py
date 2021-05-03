from django.db import models

class Patient(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    birth_date = models.DateField()
    diseases = models.TextField()
    is_active = models.BooleanField()


