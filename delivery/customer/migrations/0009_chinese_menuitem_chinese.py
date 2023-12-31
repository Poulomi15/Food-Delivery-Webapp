# Generated by Django 4.1 on 2023-01-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_menuitem_description_alter_menuitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chinese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='chinese',
            field=models.ManyToManyField(related_name='item', to='customer.chinese'),
        ),
    ]
