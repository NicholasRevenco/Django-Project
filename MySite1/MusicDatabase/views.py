from django.shortcuts import render
from django.db import connection, connections

# Create your views here.

def index(request):
    sqlQuery = "Select artist.id, artist.Name, artist.Formed from artist order by Name asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        connection.close()

    return render(request, "MusicDatabase/index.html", {
    "artists": rows
    })