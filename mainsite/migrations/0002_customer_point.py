# Generated by Django 3.0.1 on 2019-12-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='point',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
