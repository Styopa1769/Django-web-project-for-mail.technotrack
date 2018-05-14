# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse, render, get_object_or_404, redirect
from .models import Like
from django import forms
from django.views.generic import UpdateView, CreateView, View

from django.shortcuts import render

class LikeCreate(CreateView):

    model = Like
    fields = 'liked',

    def form_valid(self, form):
        form.instance = Like.object_id;
        return super(LikeCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('likes:like_create', kwargs={'pk':self.object.pk})

# Create your views here.
