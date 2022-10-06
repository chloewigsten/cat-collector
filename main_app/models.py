from django.db import models

# Create your models here.
class Breed(models.Model):

    breed=models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.breed

class Color(models.Model):

    coat = models.CharField(max_length=100, blank=True, null=True)
    pattern = models.CharField(max_length=200, blank=True, null=True)
    colors = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='colors', blank=True, null=True)

    def __str__(self):
        return self.coat

class Characteristics(models.Model): 

    traits = models.CharField(max_length=300)
    temperament = models.CharField(max_length=300)
    characteristics = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='characteristics')

    def __str__(self):
        return self.traits


class Personality(models.Model):
    traits = models.CharField(max_length=1000)
    characteristics = models.ManyToManyField(Characteristics)

    def __str__(self):
        return self.traits