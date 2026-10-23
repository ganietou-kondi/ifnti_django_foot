from django.db import models


class Match(models.Model):
    date = models.DateField()
    equipe_domiciles = models.ForeignKey(
        "Equipe", 
        on_delete=models.CASCADE,
        related_name="equipe_domiciles"
    )

    equipe_visiteurs = models.ForeignKey(
            "Equipe", 
            on_delete=models.CASCADE,
            related_name="equipe_visiteurs"
        )

    score = models.CharField(null=True)

    def __str__(self):
        return f"{self.equipe_domiciles.nom }---{ self.equipe_visiteurs.nom}: {self.score}"

class Meta:
    pass