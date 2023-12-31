# Generated by Django 4.1 on 2023-01-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_ordermodel_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
