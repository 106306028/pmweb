# Generated by Django 3.0.1 on 2019-12-26 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cost', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('safe_stock', models.IntegerField()),
                ('last_date', models.DateField()),
                ('EOQ', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order_list_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Order_list')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Product')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Supplier'),
        ),
    ]
