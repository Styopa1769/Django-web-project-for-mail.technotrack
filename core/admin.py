# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as OldUserAdmin


@admin.register(User)
class UserAdmin(OldUserAdmin):

    pass
