# Generated by Django 3.0.1 on 2020-01-02 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_user_payment_user_payment_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_payment',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='user_payment_item',
            name='payment',
        ),
    ]
