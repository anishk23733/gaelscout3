# Generated by Django 2.0.4 on 2018-04-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamindex', '0009_auto_20180420_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='order',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
