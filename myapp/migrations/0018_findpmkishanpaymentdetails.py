# Generated by Django 5.0.3 on 2024-04-03 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_findayushmancardpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindPmKishanPaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.CharField(max_length=20)),
                ('pm_kishan_id', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('upload_file', models.ImageField(upload_to='media/PmKishanPaymentDetails')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
