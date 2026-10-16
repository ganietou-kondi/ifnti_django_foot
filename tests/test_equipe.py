from tournoi.models import Equipe


def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe=Equipe.objects.create(nom="Les Lions",promo="L1")
    assert equipe.nom
    assert equipe.promo



def test_une_equipe_a_un_nom_et_une_promotion(db):
    promotion=[("l1","L1"),("l2","L2"),("l3","L3")]
    equipe=Equipe.objects.create(nom="Les Lions",promo="L4")
    assert equipe.nom
    assert equipe.promo