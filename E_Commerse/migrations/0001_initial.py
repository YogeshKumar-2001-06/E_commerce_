# Generated by Django 5.1.4 on 2024-12-22 09:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=225)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=225)),
                ('Description', models.TextField()),
                ('image', models.ImageField(upload_to='advertisement_images/')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Stock', models.IntegerField()),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisement', to='E_Commerse.category')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Order_Date', models.DateTimeField(auto_now_add=True)),
                ('Total_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPost',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=225)),
                ('Description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Discount_Price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Stock', models.IntegerField()),
                ('Image', models.ImageField(upload_to='product_images/')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='E_Commerse.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='E_Commerse.orders')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Commerse.productpost')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='E_Commerse.cart')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Commerse.productpost')),
            ],
        ),
    ]
