# Generated by Django 5.1.4 on 2024-12-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Commerse', '0004_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')]),
        ),
    ]
