# Generated by Django 4.2 on 2023-05-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_orders_alter_student_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_quality',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_quantity',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_address',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_discount',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_place_at',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_price',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
