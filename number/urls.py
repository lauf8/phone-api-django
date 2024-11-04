from django.urls import path
from number.views import NumberInvoiceView  

urlpatterns = [
    path('<int:pk>/invoice/', NumberInvoiceView.as_view(), name='number-invoice'),
]
