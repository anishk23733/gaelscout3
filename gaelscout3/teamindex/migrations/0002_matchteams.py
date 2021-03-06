# Generated by Django 2.0.4 on 2018-04-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamindex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('opr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mscore', models.DecimalField(decimal_places=2, max_digits=5)),
                ('opr_percentile', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mscore_percentile', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
