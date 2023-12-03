from django.shortcuts import render

from . import util


def index(request):
    return render(request, "sugarSpotPage/index.html", {
        "entries": util.list_entries()
    })

