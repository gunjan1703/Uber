# Generated by Django 4.2 on 2023-05-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=20, null=True)),
                ('order_price', models.CharField(blank=True, max_length=20, null=True)),
                ('order_discount', models.CharField(blank=True, max_length=20, null=True)),
                ('order_quality', models.CharField(blank=True, max_length=20, null=True)),
                ('order_address', models.CharField(blank=True, max_length=20, null=True)),
                ('order_place_at', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1),
        ),
    ]
