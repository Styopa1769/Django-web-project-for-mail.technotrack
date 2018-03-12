# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def event_detail(request, event_id):

    return HttpResponse('This is event {}'.format(event_id))
