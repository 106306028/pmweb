# Generated by Django 3.0.1 on 2020-01-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20200102_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_payment',
            name='UID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_payment_item',
            name='UID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]