# Generated by Django 5.1.2 on 2024-11-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.CharField(choices=[('JUŔIDICA', 'JUŔIDICA'), ('FÍSICA', 'FÍSICA')], default='FÍSICA', max_length=10),
        ),
    ]
