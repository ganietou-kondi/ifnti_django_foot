import pytest

from tournoi.models import Equipe, Match


def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe=Equipe.objects.create(nom="Les Lions",promo="L1")
    assert equipe.nom
    assert equipe.promo



def test_deux_equipe_ne_porte_pas_le_meme_nom(db):
    Equipe.objects.create(nom="Les Eperviers",promo="L2")
    with pytest.raises(Exception):  # noqa: B017
        Equipe.objects.create(nom="Les Eperviers",promo="L3")


def test_une_equipe_saffiche_par_son_nom(db):
    equipe=Equipe.objects.create(nom="Les Aigles",promo="L2")
    assert str(equipe)=="Les Aigles"


def test_un_match_oppose_une_equipe_a_domicile_et_une_equipe_visiteuse_a_une_date(db):
    equipe_domiciles=Equipe.objects.create(nom="Gouni",promo="L2") 
    equipe_visiteurs=Equipe.objects.create(nom="Guepard",promo="L3")   
    

    match=Match.objects.create(
        equipe_domiciles=equipe_domiciles,
        equipe_visiteurs=equipe_visiteurs,
        date="2024-06-01"

    )
    assert match.equipe_domiciles==equipe_domiciles
    assert match.equipe_visiteurs==equipe_visiteurs
    assert match.date=="2024-06-01"   


def test_un_match_nest_pas_jouer_son_score_inconnus(db):
    lions = Equipe.objects.create(nom="Les Lions", promo="L2")
    aigles = Equipe.objects.create(nom="Les Aigles", promo="L2")

    match_joue = Match.objects.create(
        equipe_domiciles=lions,
        equipe_visiteurs=aigles,
        score_domicile=2,
        score_exterieur=1,
        est_joue=True  
    )
    assert str(match_joue) == "Les Lions – Les Aigles : 2-1"

    match_a_jouer = Match.objects.create(
        equipe_domiciles=lions,
        equipe_visiteurs=aigles,
        est_joue=False
    )
    assert str(match_a_jouer) == "Les Lions – Les Aigles : à jouer"


def test_match_score_de_lequipe_qui_reçoit(db):
    lions = Equipe.objects.create(nom="Les Lions", promo="L2")
    aigles = Equipe.objects.create(nom="Les Aigles", promo="L2")

    match_joue = Match.objects.create(
        equipe_domiciles=lions,
        equipe_visiteurs=aigles,
        equipe_domiciles=2,
        score_exterieur=1,
        est_joue=True
    )
    assert str(match_joue) == "Les Lions – Les Aigles : 2-1"

    match_a_jouer = Match.objects.create(
        equipe_domiciles=lions,
        equipe_visiteurs=aigles,
        score_domicile=None,
        score_exterieur=None,
        est_joue=False
    )
    assert str(match_a_jouer) == "Les Lions – Les Aigles : à jouer"
    assert match_a_jouer.score_domicile is None
    assert match_a_jouer.score_exterieur is None

