# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def profile_details(request, pk=None):

    context = {}
    context['user'] = {
        'name': 'Styopa',
        'id': pk,
    }
    return render(request, 'profiles/profile_detail.html', context)
    return HttpResponse('This is event {} page'.format(pk))