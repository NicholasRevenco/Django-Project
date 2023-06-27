from django.shortcuts import render
from django.http import  HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

monthlyGoals = {
    "january":"Hello from January",
    "febuary":"Hello from Febuary",
    "march":"Hello from March",
    "april":"Hello from April",
    "may":"Hello from May",
    "june":"Hello from June",
    "july":"Hello from July",
    "august":"Hello from August",
    "september":"Hello from September",
    "october":"Hello from October",
    "november":"Hello from November",
    "december":"Hello from December"
}

def index(request):
    #dataToReturn = ""
    months = list(monthlyGoals.keys())
    
    #for item in months:
    #    monthPath = "/challenges/" + item
    #    dataToReturn += f"<li style='color: red; font-size: 30;'><a href='{monthPath}'>{item.capitalize()}</a></li>"

    #responseData = f"<ul>{dataToReturn}</ul>"
    #return HttpResponse(responseData)

    return render(request, "challenges/index.html", {
        "months_key":months})

def monthly_goal_by_number(request, month):
    #return HttpResponse(f"Numeric month request: {month}")
    months = list(monthlyGoals.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("You entered an invalid numeric month")
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_goal(request, month):
    try:
        strToReturn = monthlyGoals[month]
        #return HttpResponse(strToReturn)
        return render(request, 'challenges/challenge.html', {
            "text":strToReturn,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<strong>Error! Month not valid</strong>")