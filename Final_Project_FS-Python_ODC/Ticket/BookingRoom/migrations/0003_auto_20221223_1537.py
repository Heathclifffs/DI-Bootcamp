# Generated by Django 2.2.16 on 2022-12-23 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingRoom', '0002_resevationmovie_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resevationplate',
            name='Heure',
        ),
        migrations.AddField(
            model_name='resevationplate',
            name='Created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2022, 12, 23)),
            preserve_default=False,
        ),
    ]
