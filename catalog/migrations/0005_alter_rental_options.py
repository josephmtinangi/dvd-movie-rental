# Generated by Django 4.1.7 on 2023-05-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rental_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set movie as returned'),)},
        ),
    ]
