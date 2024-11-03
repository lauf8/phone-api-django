
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from call.models import Call, CallRegister
from call.serializers import CallInvoceSerializer, CallRegisterSerializer, CallSerializer
from call.manager import CallManager
from rest_framework.views import APIView

class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class CallRegsiterViewSet(viewsets.ModelViewSet):
    queryset = CallRegister.objects.all()
    serializer_class = CallRegisterSerializer
    


class CallInvoiceView(APIView):
    def get(self, request, pk):  
        call = get_object_or_404(Call, pk=pk)
        call_manager = CallManager(call=call)
        invoice = call_manager.call_invoice_data()
        serializer = CallInvoceSerializer(data=invoice)  
        serializer.is_valid(raise_exception=True)  # Valida os dados

        return Response(serializer.data, status=status.HTTP_200_OK)