# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Event


def events_list(request):

    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/events_list.html', context)


def event_detail(request, pk=None):

    event = get_object_or_404(Event, id = pk)
    context = {
        'event': event
    }
    return render(request, 'events/event_detail.html', context)
