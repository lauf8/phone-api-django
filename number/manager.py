from datetime import datetime
from call.models import Call, CallRegister
from number.models import Number
from utils.last_month import get_last_month
from call.manager import CallManager


class NumberManager():
    
    def __init__(self, number:Number):
        self.number = number
    
    def calls_month(self,year: int,month:int):
        ended_calls = CallRegister.objects.filter(
        type='END',
        timestamp__year=year,
        timestamp__month=month,
        call_id__source=self.number)
        return ended_calls
    
    def number_invoice(self,year=None,month=None):
        if not year and  not month:
            year,month = get_last_month()
        calls = self.calls_month(year=int(year),month=int(month))
        invoices = []
        for call in calls:
            call_object = Call.objects.get(pk=call.call_id.pk)
            call_manager = CallManager(call=call_object)
            invoice = call_manager.call_invoice_data()
            
            if invoice is not None:
                invoices.append(invoice)
            
            
        return invoices
            
        

        
        
    