# Generated by Django 3.2.5 on 2021-09-19 15:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20210919_1521'),
        ('users', '0001_initial'),
        ('orders', '0002_alter_shoppingcart_number_of_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_captured',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shopping_cart',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='applied_discount_percentage',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED'), ('TRANSIT', 'TRANSIT'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=16),
        ),
        migrations.CreateModel(
            name='OrderSession',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('payment_captured', models.BooleanField(default=False)),
                ('final_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tax_percentage', models.DecimalField(decimal_places=2, default=18.0, max_digits=4)),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shoppingcart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='orders.ordersession'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order_session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='orders.ordersession'),
        ),
    ]
