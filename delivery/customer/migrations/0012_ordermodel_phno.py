# Generated by Django 4.1 on 2023-04-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_contact_remove_menuitem_chinese_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phno',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]