from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    numero = models.CharField(max_length=10 , unique=True)
    capacite = models.IntegerField()
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return f"Table {self.numero} - {self.capacite} Personne"
    
class Menu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to='menu_images/', null=True, blank=True) 
    disponible = models.BooleanField(default=True)


    def __str__(self):
        return f"Menu {self.nom} - {self.prix}"

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservation")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservation")
    date = models.DateField()
    heure = models.TimeField()
    statut = models.CharField(max_length=30, default="En attente")
    menu = models.ManyToManyField(Menu, related_name="reservations")

    def __str__(self):
        return f"Reservation {self.id} {self.utilisateur.username} - {self.table}"

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact {self.id} - {self.nom}"



class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    heure = models.TimeField()
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image= models.ImageField(upload_to='menu_images/', null=True, blank=True) 

    def __str__(self):
        return f"Evenement {self.nom} - {self.date}"