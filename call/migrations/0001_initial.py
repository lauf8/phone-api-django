# Generated by Django 5.1.2 on 2024-11-03 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('number', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('START', 'START'), ('END', 'END')], default='START', max_length=6)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.BigIntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='number.number')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination', to='number.number')),
            ],
        ),
    ]