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

def player_by_number(request, player):
    roster = list(player_roster.keys())
    if player > len(roster) or player < 1:
        return HttpResponseNotFound("You entered an invalid numeric player's number")
    next_player = roster[player-1]
    return HttpResponseRedirect("/BaltimoreRavens/" + next_player)

def player_text(request, player):
    try:
        strToReturn = player_roster[player]
        return render(request, 'BaltimoreRavens/player_account.html', {
            "text":strToReturn,
            "player_name": player.capitalize()
        })
    except:
        return HttpResponseNotFound("Player not valid!")