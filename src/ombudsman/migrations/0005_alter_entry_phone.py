# Generated by Django 3.2.3 on 2021-05-23 12:22

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ombudsman', '0004_interaction_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, verbose_name='phone'),
        ),
    ]
