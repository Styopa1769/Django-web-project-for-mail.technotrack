# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse, render, get_object_or_404, redirect
from .models import Event
from django import forms
from django.views.generic import UpdateView, CreateView
from django.http import JsonResponse


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = 'name',


class EventCreate(CreateView):
    model = Event
    fields = 'name',
    template_name = 'events/event_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(EventCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.object.pk})


class EventEdit(UpdateView):
    model = Event
    fields = 'name', 'destination', 'departurePoint'
    template_name = 'events/event_edit.html'

    def get_success_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.object.pk})


class EventsListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('name', 'Name'),
        ('id', 'ID'),
    ), required=False)
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
    event = get_object_or_404(Event, id=pk)
    context = {
        'event': event
    }
    return render(request, 'events/event_detail.html', context)


def thisIsEvent(request):
    name = Event.objects.last().name
    return JsonResponse({'event': name})
