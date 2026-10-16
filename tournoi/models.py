from django.db import models  # noqa: F401

class Equipe(models.Model):
    nom = models.CharField(max_length=120)
    promo = models.CharField(max_length=120)



class Meta:
    pass



