# Generated by Django 3.0.3 on 2020-09-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200918_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]