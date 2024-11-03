from datetime import datetime, timedelta
from call.models import Call, CallRegister
from datetime import time

class CallManager:
    
    def __init__(self, call:Call):
        self.call = call
        
    def call_find_end_start(self) -> tuple:
        """
        Return the call's start and end register
        """
        start = CallRegister.objects.filter(call_id=self.call, type='START').first()
        end = CallRegister.objects.filter(call_id=self.call, type='END').first()
        return start,end
    
    def call_start_date_time(self)-> tuple:
        """"
        Returns the date and time of the call
        """
        start, end = self.call_find_end_start()
        start_date = start.timestamp.date()
        start_hour = start.timestamp.time()
        return start_date, start_hour
        
    
    def duration(self,start,end):
        duration = end - start
        duration_seconds = timedelta(seconds=duration.total_seconds())
        return duration_seconds
        
    
    def call_duration_seconds(self) -> timedelta:
        """
        Return the duration of the call in seconds.
        """
        start, end = self.call_find_end_start()
        duration_seconds = self.duration(start = start.timestamp,end= end.timestamp)
        
        return duration_seconds

    def call_duration(self) -> str:
        """
        Return the duration of the call in the format `0h0m0s`.
        """
        seconds = self.call_duration_seconds()
        hours, remainder = divmod(seconds.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes)}m{int(seconds)}s"
    
    def call_invoice(self)-> float:
        """
        Return the call's cost.
        """
        invoice = 0.36
        tax = 0.09 
        start, end = self.call_find_end_start()
        
        start_time = start.timestamp.time()
        end_time = end.timestamp.time()
        
        nortune_time_start = time(22, 0, 0) 
        noturne_time_end = time(6, 0, 0)
        
        if (start_time > nortune_time_start or start_time < noturne_time_end) and (end_time > nortune_time_start or end_time < noturne_time_end):
            return invoice
        
        #time beetween 22 - 06
        if start_time > nortune_time_start or start_time < noturne_time_end:
            start_time = noturne_time_end
            
        if end_time > nortune_time_start or end_time < noturne_time_end:
            end_time = nortune_time_start
        
        start_datetime = datetime.combine(datetime.today(), start_time)
        end_datetime = datetime.combine(datetime.today(), end_time)
        
        duration = self.duration(start_datetime,end_datetime)
        
        minutes, seconds = divmod(duration.total_seconds(), 60)
        
        if seconds > 0:
            minutes += 1
            
        call_tax = minutes * tax
        invoice = call_tax + invoice
        
        return invoice
        
    def call_invoice_data(self) -> dict:
        """
        Return invoice's data
        """
        source = self.call.source
        date, time = self.call_start_date_time()
        duration = self.call_duration()
        value = self.call_invoice()
        
        call_invoice_date = {
            "source": source,
            "date": date,
            "time": time,
            "duration": duration,
            "value": value
        }
        return call_invoice_date
        
        
        
        
        
        
        
        