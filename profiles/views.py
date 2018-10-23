# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from core.models import User
from django.shortcuts import render

# Create your views here.


def profile_details(request, pk=None):

    context = {}
    user = User.objects.get(id=pk)
    context['user'] = {
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'id': pk,
        'name': user.username,
    }
    return render(request, 'profiles/profile_detail.html', context)