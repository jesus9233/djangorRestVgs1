# Generated by Django 3.1 on 2020-08-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creditCardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField()),
                ('card_number', models.CharField(max_length=10)),
                ('exp_date', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=10)),
            ],
        ),
    ]
