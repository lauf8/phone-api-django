from django.shortcuts import render
from number.models import Number
from rest_framework import viewsets
from number.serializers import NumberSerializer


class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer