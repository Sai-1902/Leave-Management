# Generated by Django 4.2.5 on 2024-01-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leaves', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='Employee_Id',
            field=models.IntegerField(default=30),
        ),
    ]