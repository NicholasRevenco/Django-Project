from django.shortcuts import render
from django.http import  HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "BaltimoreRavens/index.html")

player_roster = {
    "Lamar Jackson 1":{'name': 'Lamar Jackson 1', 'title': 'linebacker', 'number': '1', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3916387.png&w=350&h=254'},
    "Lamar Jackson 2":{'name': 'Lamar Jackson 2', 'title': 'kicker', 'number': '2', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3916387.png&w=350&h=254'},
    "Lamar Jackson 3":{'name': 'Lamar Jackson 3', 'title': 'Quarterback', 'number': '5', 'image': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/3916387.png&w=350&h=254'}
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
            "text": player_roster[player],
            "player_name": player.capitalize()
        })
    except:
        return HttpResponseNotFound("Player not valid!")