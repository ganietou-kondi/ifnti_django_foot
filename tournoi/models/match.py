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

    score_domicile = models.CharField(null=True)
    score_exterieure = models.CharField(null=True)
    est_joue = models.BooleanField()

    def __str__(self):
        if self.statut:
            return f"{self.equipe_domiciles.nom }---{ self.equipe_visiteurs.nom}: {self.score_domicile}:{self.score_exterieure}"
        else:
            return f"{self.equipe_domiciles.nom }---{ self.equipe_visiteurs.nom}: à jouer"

class Meta:
    pass