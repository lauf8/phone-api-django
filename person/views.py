from django.shortcuts import render
from person.models import Person
from rest_framework import viewsets
from person.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer