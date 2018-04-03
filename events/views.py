# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from django import forms


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = 'name',


def event_create(request):
    event = Event()

    if request.method == 'GET':
        form = EventForm(instance=event)
        return render(request,
                      'events/event_create.html',
                      {'form': form}
                      )
    elif request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('events:event_detail', pk=event.id)
        else:
            return render(request,
                          'events/event_create.html',
                          {'form': form}
                          )


def event_edit(request, pk=None):

    event = get_object_or_404(Event, id=pk, author=request.user)
    if request.method == 'GET':
        form = EventForm(instance=event)
        return render(request,
                      'events/event_edit.html',
                      {'form': form, 'event': event}
                      )
    elif request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('events:event_detail', pk=event.id)
        else:
            return render(request,
                          'events/event_edit.html',
                          {'form': form, 'event': event}
                          )


class EventsListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name'),
        ('id', 'ID'),
    ),required=False)
    search = forms.CharField(required=False)


def events_list(request):
    events = Event.objects.all()
    form = EventsListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            events = events.order_by(data['sort'])
        if data['search']:
            events = events.filter(name__icontains=data['search'])
    context = {
        'events': events
    }
    return render(request, 'events/events_list.html', context)


def event_detail(request, pk=None):

    event = get_object_or_404(Event, id = pk)
    context = {
        'event': event
    }
    return render(request, 'events/event_detail.html', context)
