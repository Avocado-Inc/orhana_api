# Generated by Django 3.2.5 on 2021-07-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]