from django.db import models

# Create your models here.


class airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class flight(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.origin} to {self.destination}"

class passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(flight, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

