from django.shortcuts import render
from django.http import  HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "BaltimoreRavens/index.html")

player_roster = {
    "Lamar Jackson":{'name': 'Lamar Jackson', 'position': 'Quarterback', 'number': '8', 'height': '6 2', 'weight': '212 lbs', 'college': 'Louisville', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3916387.png&w=350&h=254'},
    "Tyler Huntley":{'name': 'Tyler Huntley', 'position': 'Quarterback', 'number': '2', 'height': '6 1', 'weight': '196 lbs', 'college': 'Utah', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/4035671.png&w=350&h=254'},
    "Anthony Brown":{'name': 'Anthony Brown', 'position': 'Quarterback', 'number': '12', 'height': '6 1', 'weight': '228 lbs', 'college': 'Oregon', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/4035312.png&w=350&h=254'}
}

def index(request):
    roster = player_roster.keys()

    return render(request, "BaltimoreRavens/index.html", {
        "text": player_roster.values(),
        "roster_key":roster,
        "player_roster": player_roster

        })

def player_by_number(request, player):
    roster = player_roster.keys()
    if player > len(roster) or player < 1:
        return HttpResponseNotFound("You entered an invalid numeric player's number")
    next_player = roster[player-1]
    return HttpResponseRedirect("/BaltimoreRavens/" + next_player)

def player_text(request, player):
    try:
        return render(request, 'BaltimoreRavens/player_account.html', {
            "player_roster": player_roster[player],
        })
    except:
        return HttpResponseNotFound("Player not valid!")