from django.db import models
from django.forms import ValidationError
from number.models import Number


class Call(models.Model):
    source = models.ForeignKey(Number,on_delete=models.DO_NOTHING,related_name='source')
    destination = models.ForeignKey(Number,on_delete=models.DO_NOTHING,related_name='destination')
    
    def __str__(self) -> str:
        return f"{self.source} - {self.destination}"
    
    
class CallRegister(models.Model):
    TYPE_CALL = [
        ('START', 'START'),
        ('END', 'END'),
    ]
    type = models.CharField(
        max_length=6,
        choices=TYPE_CALL,
        default='START',
    )
    timestamp = models.DateTimeField()
    call = models.ForeignKey(Call,on_delete=models.DO_NOTHING)
    
    def clean(self):
        if CallRegister.objects.filter(call=self.call, type=self.type).exists():
            raise ValidationError(f"Já existe um registro do tipo '{self.type}' para essa chamada.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)