from django.shortcuts import render
from django.http import  HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "BaltimoreRavens/index.html")

player_roster = {
    "Lamar Jackson":["Text1", "Text2", "Text3"],
    "Lamar Jackson 2":["Text1", "Text2", "Text3"]
}

def index(request):
    roster = list(player_roster.keys())

    return render(request, "BaltimoreRavens/index.html", {
        "roster_key":roster})