# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Place
from django import forms


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = 'name',


def place_create(request):
    place = Place()

    if request.method == 'GET':
        form = PlaceForm(instance=place)
        return render(request,
                      'places/place_create.html',
                      {'form': form}
                      )
    elif request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.save()
            return redirect('places:place_detail', pk=place.id)
        else:
            return render(request,
                          'places/place_create.html',
                          {'form': form}
                          )


def place_edit(request, pk=None):

    place = get_object_or_404(Place, id=pk, author=request.user)
    if request.method == 'GET':
        form = PlaceForm(instance=place)
        return render(request,
                      'places/place_edit.html',
                      {'form': form, 'place': place}
                      )
    elif request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            event = form.save()
            return redirect('places:place_detail', pk=event.id)
        else:
            return render(request,
                          'places/palce_edit.html',
                          {'form': form, 'place': place}
                          )


class PlacesListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name'),
        ('id', 'ID'),
    ),required=False)
    search = forms.CharField(required=False)


def places_list(request):
    places = Place.objects.all()
    form = PlacesListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            places = places.order_by(data['sort'])
        if data['search']:
            places = places.filter(name__icontains=data['search'])
    context = {
        'places': places
    }
    return render(request, 'places/places_list.html', context)


def place_detail(request, pk=None):

    place = get_object_or_404(Place, id = pk)
    context = {
        'place': place
    }
    return render(request, 'places/place_detail.html', context)