# Generated by Django 3.0.1 on 2019-12-29 15:54

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
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ingre_MRP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrpStr', models.CharField(max_length=20)),
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
                ('TL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='inter_MRP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrpStr', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('stock', models.IntegerField()),
                ('safe_stock', models.IntegerField()),
                ('TL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpsStr', models.CharField(max_length=20)),
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
                ('TL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_MRP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrpStr', models.CharField(max_length=20)),
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
                ('intermediate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Intermediate')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='element',
            field=models.ManyToManyField(through='mainsite.Product_element', to='mainsite.Intermediate'),
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
            model_name='order_list',
            name='product',
            field=models.ManyToManyField(through='mainsite.Order_list_detail', to='mainsite.Product'),
        ),
        migrations.CreateModel(
            name='Intermediate_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Ingredient')),
                ('intermediate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Intermediate')),
            ],
        ),
        migrations.AddField(
            model_name='intermediate',
            name='element',
            field=models.ManyToManyField(through='mainsite.Intermediate_element', to='mainsite.Ingredient'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Supplier'),
        ),
    ]
