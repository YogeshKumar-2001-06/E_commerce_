# Generated by Django 5.1.4 on 2024-12-29 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerse', '0023_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='Cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='Product',
        ),
        migrations.RemoveField(
            model_name='productpost',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Advertisement',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='ProductPost',
        ),
    ]
