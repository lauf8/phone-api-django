from django.core.exceptions import ValidationError
from django.test import TestCase
from person.models import Person
from .models import Number

class NumberModelTest(TestCase):

    def setUp(self):
        
        self.owner = Person.objects.create(
            name="Carlos Silva",
            address="Rua Principal, 123",
            email="carlos.silva@example.com",
            type="FÍSICA",
            register="12345678909",
        )
    
    def test_create_number(self):
        
        number = Number.objects.create(number="12345678901", owner=self.owner)
        self.assertEqual(number.number, "12345678901")
        self.assertEqual(number.owner, self.owner)
        self.assertEqual(str(number), "12345678901")

    def test_unique_number(self):
        
        Number.objects.create(number="12345678901", owner=self.owner)
        with self.assertRaises(ValidationError):
            duplicate_number = Number(number="12345678901", owner=self.owner)
            duplicate_number.full_clean()
            duplicate_number.save()

    def test_str_representation(self):
        
        number = Number.objects.create(number="98765432101", owner=self.owner)
        self.assertEqual(str(number), "98765432101")
