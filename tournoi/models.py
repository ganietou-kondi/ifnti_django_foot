from django.db import models  # noqa: F401

class Equipe(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    promo = models.CharField(max_length=120)

    
    def __str__(self):
        return self.nom 

class Meta:
    pass



