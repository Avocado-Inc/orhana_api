# Generated by Django 3.2.5 on 2021-07-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='number_of_products',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='number_of_products',
            field=models.BigIntegerField(default=0),
        ),
    ]
