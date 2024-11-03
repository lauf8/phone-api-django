from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150)
    address = models.TextField()
    email = models.EmailField()
    TYPE_PERSON = [
        ('JUŔICA', 'JUŔICA'),
        ('FÍSICA', 'FÍSICA'),
    ]
    type = models.CharField(
        max_length=6,
        choices=TYPE_PERSON,
        default='FÍSICA',
    )
    #this field depends on the type of person, if the person is natural CPF, if is a company CNPJ
    register = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name} - {self.register}"
    

