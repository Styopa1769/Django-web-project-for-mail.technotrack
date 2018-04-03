# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView


def index(request):

    return render(request, 'core/main.html')

class Login(LoginView):

    template_name = 'core/login.html'

class Logout(LogoutView):

    template_name = 'core/logout.html'