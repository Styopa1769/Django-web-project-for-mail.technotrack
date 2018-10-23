from django.shortcuts import render
from jsonrpc import jsonrpc_method
from jsonrpc import Error

from django.core.serializers import serialize

from events.models import Event, EventForm

import json


@jsonrpc_method('api.hello')
def say_hello(request, name):
    return "Hello, {}".format(name)


@jsonrpc_method('api.event_list')
def get_events(request):
    return json.loads(serialize('json', Event.objects.all()))


@jsonrpc_method('api.add_event')
def add_event(request, **kwargs):
    name = kwargs.get('name')
    if name is None:
        raise Error('No "name" field')
    form = EventForm(kwargs)
    if not form.is_valid():
        raise Error('Not valid form')
    event = Event.objects.filter(name=name).first()
    if event is not None:
        raise Error('The event with the same name exists')
    form.save()
    return 'success'
