# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def profile_details(response, user_id):

    return HttpResponse('Hello user with id {}'.format(user_id))