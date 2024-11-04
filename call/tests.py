from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.test import TestCase
from number.models import Number
from call.models import Call, CallRegister
from person.models import Person



class CallModelTest(TestCase):
    
    def setUp(self):
        owner = Person.objects.create(
            name="Carlos Silva",
            address="Rua Principal, 123",
            email="carlos.silva@example.com",
            type="FÍSICA",
            register="12345678909",
        )
        self.number1 = Number.objects.create(number="12345678901", owner= owner)
        self.number2 = Number.objects.create(number="98765432101", owner= owner)
    
    def test_create_call(self):
        call = Call.objects.create(source=self.number1, destination=self.number2)
        self.assertEqual(call.source, self.number1)
        self.assertEqual(call.destination, self.number2)
        self.assertEqual(str(call), f"{self.number1} - {self.number2}")

class CallRegisterModelTest(TestCase):

    def setUp(self):
        owner1 = Person.objects.create(
            name="Carlos Silva",
            address="Rua Principal, 123",
            email="carlos.silva@example.com",
            type="FÍSICA",
            register="12345678909",
        )
        owner2 = Person.objects.create(
            name="Pablo da Silva",
            address="Rua Principal, 123",
            email="carlos.silva@example.com",
            type="FÍSICA",
            register="1234567839",
        )
        self.number1 = Number.objects.create(number="12345678901", owner= owner1)
        self.number2 = Number.objects.create(number="98765432101", owner= owner2)
        self.call = Call.objects.create(source=self.number1, destination=self.number2)
    
    def test_create_call_register_start(self):
        timestamp = timezone.make_aware(datetime(2024, 1, 1, 10, 0, 0))
        call_register = CallRegister.objects.create(type='START', timestamp=timestamp, call=self.call)
        self.assertEqual(call_register.type, 'START')
        self.assertEqual(call_register.timestamp.strftime('%Y-%m-%d %H:%M:%S'), '2024-01-01 10:00:00')
        self.assertEqual(call_register.call, self.call)

    def test_create_call_register_end(self):
        timestamp = timezone.make_aware(datetime(2024, 1, 1, 10, 5, 0))
        call_register = CallRegister.objects.create(type='END', timestamp=timestamp, call=self.call)
        self.assertEqual(call_register.type, 'END')
        self.assertEqual(call_register.timestamp.strftime('%Y-%m-%d %H:%M:%S'), '2024-01-01 10:05:00')
        self.assertEqual(call_register.call, self.call)

    def test_unique_call_register_type(self):
        CallRegister.objects.create(type='START', timestamp='2024-01-01 10:00:00', call=self.call)
        with self.assertRaises(ValidationError):
            call_register = CallRegister(type='START', timestamp='2024-01-01 10:05:00', call=self.call)
            call_register.full_clean()
            call_register.save()

    def test_unique_call_register_type_end(self):
        CallRegister.objects.create(type='END', timestamp='2024-01-01 10:05:00', call=self.call)
        with self.assertRaises(ValidationError):
            call_register = CallRegister(type='END', timestamp='2024-01-01 10:10:00', call=self.call)
            call_register.full_clean()
            call_register.save()
