# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Place


def places_list(request):

    context = {
        'places': Place.objects.all()
    }
    return render(request, 'places/places_list.html', context)


def place_detail(request, pk=None):

    place = get_object_or_404(Place, id = pk)
    context = {
        'place': place
    }
    return render(request, 'places/place_detail.html', context)