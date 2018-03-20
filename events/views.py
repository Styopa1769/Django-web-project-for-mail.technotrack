# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Event

def event_detail(request, event_id):

    return HttpResponse('This is event {} detail page'.format(event_id))


def events_list(request):

    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/events_list.html', context)
    return HttpResponse('This is events page')


def event_detail(request, pk=None):

    context = {
        'event': Event.objects.get(id=pk)
    }
    return render(request, 'events/event_detail.html', context)
    return HttpResponse('This is event {} page'.format(event_id))
