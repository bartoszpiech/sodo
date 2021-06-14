from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Room(models.Model):
    number = models.IntegerField('Numer')
    amount_of_beds = models.IntegerField('Liczba łóżek')
    price = models.FloatField('Cena')
    balcony = models.BooleanField('Balkon')
    def __str__(self):
        return str(self.number)
    def get_absolute_url(self):
        return reverse('database-room-detail', kwargs={'pk': self.pk})

class Client(models.Model):
    first_name = models.CharField('Imię', max_length = 100)
    last_name = models.CharField('Nazwisko', max_length = 100)
    tel_number = models.CharField('Numer telefonu', max_length = 20)
    email = models.EmailField('Adres E-mail')
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def get_absolute_url(self):
        return reverse('database-client-detail', kwargs={'pk': self.pk})

class Patient(models.Model):
    first_name = models.CharField('Imię', max_length = 100)
    last_name = models.CharField('Nazwisko', max_length = 100)
    birth_date = models.DateField('Data urodzenia')
    diseases = models.TextField('Choroby')
    is_active = models.BooleanField('Aktywny')
    room = models.ForeignKey(Room, null = True, on_delete = models.CASCADE, verbose_name = 'Pokój', related_name = 'patients')
    client = models.OneToOneField(Client, null = True, on_delete = models.CASCADE, verbose_name = 'Klient')

    #showonly_active = False

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def get_absolute_url(self):
        return reverse('database-patient-detail', kwargs={'pk': self.pk})
    def total_medicine_sum(self):
        result = 0
        for medicine in self.medicines.all():
            result = result + medicine.price
        return result
    """
    def toggle_showonly_active(self):
        self.showonly_active = True
        """




class Medicine(models.Model):
    name = models.CharField('Nazwa', max_length = 100)
    active_substance = models.CharField('Substancja aktywna', max_length = 100)
    price = models.FloatField('Cena [zł]')
    dose = models.FloatField('Dawka [g]')
    times_a_day = models.IntegerField('Razy dziennie')
    patient = models.ForeignKey(Patient, null = True, on_delete = models.CASCADE, related_name = 'medicines')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('database-medicine-detail', kwargs={'pk': self.pk})

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Imię', max_length = 100)
    last_name = models.CharField('Nazwisko', max_length = 100)
    email = models.EmailField('Adres E-mail')
    tel_number = models.CharField('Numer telefonu', max_length = 20)
    salary = models.FloatField('Stawka')
    def __str__(self):
        return self.first_name + ' ' + self.last_name
