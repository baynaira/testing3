# Generated by Django 5.0.6 on 2024-05-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
