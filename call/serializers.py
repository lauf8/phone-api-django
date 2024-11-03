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


class CallInvoceSerializer(serializers.Serializer):
    
    source = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()
    duration = serializers.CharField(max_length=10)
    value = serializers.FloatField()
    
