from django.shortcuts import render
from django.db import connection, connections

# Create your views here.

def index(request):
    sqlQuery = "Select artist.id, artist.Name, artist.Formed, artist.Website from artist order by artist.id asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/index.html", {
    "artists": rows
    })

def indexWithSort(request, sort):

    if sort == "name":
        sqlQuery = "Select artist.id, artist.Name, artist.Formed from artist order by artist.Name asc"
    elif sort == "id":
         sqlQuery = "Select artist.id, artist.Name, artist.Formed from artist order by artist.id asc"
    elif sort == "formed":
         sqlQuery = "Select artist.id, artist.Name, artist.Formed from artist order by artist.formed asc"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/index.html", {
    "artists": rows
    })

def idAlbums(request, idNum):
    sqlQuery = "Select artist.id, album.id, artist.Name, album.albumName, album.YearReleased from artist inner join album on artist.id = album.artistId where artist.id =" + str(idNum)
    print(sqlQuery)
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/albums.html", {
    "artists": rows
    })

def idAlbums(request, idNum):
    sqlQuery = "Select artist.id, album.id, artist.Name, album.albumName, album.YearReleased from artist inner join album on artist.id = album.artistId where artist.id =" + str(idNum)
    print(sqlQuery)
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "MusicDatabase/albums.html", {
    "artists": rows
    })