# Generated by Django 5.0.3 on 2024-04-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_amountset_amount1_alter_amountset_amount10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='findpancard',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='findpancard',
            name='paid',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='findpancard',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
