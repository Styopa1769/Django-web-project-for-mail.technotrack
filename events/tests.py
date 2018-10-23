# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.test import TestCase, Client

from django.contrib.auth.models import User
from events.models import Event

from django.test import TestCase


# Create your tests here.

class TestEntryList(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(username='test_user', email='test_email')
        self.event = Event.objects.create(name='testEvent')

    def test_entry_list(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)