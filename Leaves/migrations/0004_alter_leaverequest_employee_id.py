# Generated by Django 4.2.5 on 2024-01-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leaves', '0003_leaverequest_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='Employee_Id',
            field=models.CharField(max_length=20),
        ),
    ]
