from django.db import models
from person.models import Person


class Number(models.Model):
    number = models.CharField(max_length=12, unique=True)
    owner = models.ForeignKey(Person,on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.number
