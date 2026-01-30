from django.db import models

class Warzywa(models.Model):
  nazwa = models.CharField(max_length=255)
  cena = models.PositiveIntegerField()
  czy_bio = models.BooleanField(default=True)
 
class Owoce(models.Model):
  nazwa = models.CharField(max_length=255)
  cena = models.PositiveIntegerField()
  czy_bio = models.BooleanField(default=True)
  czy_suszone = models.BooleanField(default=False)

  
class Napoje(models.Model):
  nazwa = models.CharField(max_length=255)
  cena = models.PositiveIntegerField()
  czy_bio = models.BooleanField(default=True)
  objetosc = models.FloatField(help_text="w litrach, np. 0.5")
  czy_gazowany = models.BooleanField(default=False)


class Miesa(models.Model):
  nazwa = models.CharField(max_length=255)
  cena = models.PositiveIntegerField()
  czy_bio = models.BooleanField(default=True)
  rodzaj = models.CharField(max_length=50, help_text="np. Wołowina, Drób")


class Pieczywo(models.Model):
  nazwa = models.CharField(max_length=255)
  cena = models.PositiveIntegerField()
  czy_bio = models.BooleanField(default=True)
  rodzaj_maki = models.CharField(max_length=100, help_text="np. Żytnia, Pszenna")

