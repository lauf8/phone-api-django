from django.urls import path
from call.views import CallInvoiceView  

urlpatterns = [
    path('<int:pk>/invoice/', CallInvoiceView.as_view(), name='call-invoice'),
]