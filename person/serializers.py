from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'address', 'email', 'type', 'register']
