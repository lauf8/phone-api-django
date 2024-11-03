from rest_framework import serializers
from call.models import Call, CallRegister

class CallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Call
        fields = ['source', 'destination']

class CallRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CallRegister
        fields = ['type', 'timestamp','call_id']
