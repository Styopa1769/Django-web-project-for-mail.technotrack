# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def profile_details(request, user_id):

    return HttpResponse('Hello. You are user with id {}'.format(user_id))
