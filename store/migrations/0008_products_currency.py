# Generated by Django 5.1.3 on 2024-12-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_customer_is_verified_customer_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='currency',
            field=models.CharField(default='BDT', max_length=3),
        ),
    ]