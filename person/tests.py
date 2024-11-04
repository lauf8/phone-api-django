from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Person

class PersonModelTest(TestCase):

    def setUp(self):
        
        self.person_fisica_data = {
            "name": "João Silva",
            "address": "Rua das Flores, 123",
            "email": "joao.silva@example.com",
            "type": "FÍSICA",
            "register": "12345678909",  
        }
       
        self.person_juridica_data = {
            "name": "Empresa XYZ",
            "address": "Avenida Central, 456",
            "email": "contato@empresaxyz.com",
            "type": "JURÍDICA",
            "register": "12345678000199", 
        }

    def test_create_person_fisica(self):
        
        person_fisica = Person.objects.create(**self.person_fisica_data)
        self.assertEqual(person_fisica.type, "FÍSICA")
        self.assertEqual(person_fisica.register, "12345678909")
        self.assertEqual(str(person_fisica), "João Silva - 12345678909")

    def test_create_person_juridica(self):
        
        person_juridica = Person.objects.create(**self.person_juridica_data)
        self.assertEqual(person_juridica.type, "JURÍDICA")
        self.assertEqual(person_juridica.register, "12345678000199")
        self.assertEqual(str(person_juridica), "Empresa XYZ - 12345678000199")

    def test_invalid_email(self):
        
        self.person_fisica_data["email"] = "email-invalido"
        with self.assertRaises(ValidationError):
            person_fisica = Person(**self.person_fisica_data)
            person_fisica.full_clean()  # Valida o email
