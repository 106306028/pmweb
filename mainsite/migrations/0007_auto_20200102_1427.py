# Generated by Django 3.0.1 on 2020-01-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20200102_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_payment',
            name='date',
            field=models.DateTimeField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user_payment_item',
            name='date',
            field=models.DateTimeField(max_length=20),
        ),
    ]