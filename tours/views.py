from django.shortcuts import render
from django.http import Http404

def index_view (request):
    return render(request, "tours_template/index.html")

def departure_view(request, departure_id):
    departures = {
        str('msk'): "Из Москвы",
        str('spb'): "Из Петербурга",
        str('nsb'): "Из Новосибирска",
        str('ekb'): "Из Екатеринбурга",
        str('kaz'): "Из Казани",
    }
    try:
        departure = departures[departure_id]
    except KeyError:
        raise Http404
    return render(request, "tours_template/departure.html", context={
        'departure': departure,
    })


def tour_view (request, tour_id):
    tours = {
        1: "Тур №1",
        2: "Тур №2",
        3: "Тур №3",
        4: "Тур №4",
        5: "Тур №5",
    }
    try:
        tour = tours[tour_id]
    except KeyError:
        raise Http404
    return render(request, "tours_template/tour.html", context={
        'tour': tour,
    })