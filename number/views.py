from django.shortcuts import get_object_or_404
from call.serializers import CallInvoceSerializer
from number.models import Number
from rest_framework import viewsets , status
from number.serializers import NumberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from number.manager import NumberManager

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    
class NumberInvoiceView(APIView):

    def get(self, request, pk):
        number = get_object_or_404(Number, pk=pk)
        number_manager = NumberManager(number=number)
        
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        if year and month:
            invoices = number_manager.number_invoice(year=int(year), month=int(month))
        else: 
            invoices = number_manager.number_invoice()
        print(invoices)
        serializer = CallInvoceSerializer(data=invoices)  
        serializer.is_valid(raise_exception=True)
        return Response(invoices, status=status.HTTP_200_OK)