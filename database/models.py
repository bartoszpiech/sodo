from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    amount_of_beds = models.IntegerField()
    price = models.FloatField()
    balcony = models.BooleanField()
    def __str__(self):
        return str(self.number)

class Client(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    tel_number = models.CharField(max_length = 20)
    email = models.EmailField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Patient(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    diseases = models.TextField()
    is_active = models.BooleanField()
    room = models.ForeignKey(Room, null = True, on_delete = models.CASCADE)
    client = models.OneToOneField(Client, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Medicine(models.Model):
    name = models.CharField(max_length = 100)
    active_substance = models.CharField(max_length = 100)
    price = models.FloatField()
    dose = models.FloatField()
    times_a_day = models.IntegerField()
    patient = models.ForeignKey(Patient, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.name
