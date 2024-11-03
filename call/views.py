from rest_framework import viewsets
from call.models import Call, CallRegister
from call.serializers import CallRegisterSerializer, CallSerializer


class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class CallRegsiterViewSet(viewsets.ModelViewSet):
    queryset = CallRegister.objects.all()
    serializer_class = CallRegisterSerializer