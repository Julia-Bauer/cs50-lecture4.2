from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    #on_delete=CASCADE --> se um aeroporto for deletado, todos os voo dele também são
    #related name --> forma de acessar uma relação em uma ordem reversa
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")

    #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"