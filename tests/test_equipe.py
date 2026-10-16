from tournoi.models import Equipe


def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe=Equipe.objects.create(nom="Les Lions",promo="L1")
    assert equipe.nom
    assert equipe.promo



def test_deux_equipe_ne_porte_pas_le_meme_nom(db):
    equipe=Equipe.objects.create(nom="Les Eperviers",promo="L2")
    with pytest.raises(Exception):
        Equipe .objects.create(nom="Les Eperviers",promo="L3")