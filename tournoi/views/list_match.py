from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401

from tournoi.models.match import Match


def list_match(request):
    return render(
        request,
        "tournoi/list_match.html",
        {"matchs": Match.object.all()},
    )





    