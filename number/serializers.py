from rest_framework import serializers
from number.models import Number

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Number
        fields = ['number', 'owner']
