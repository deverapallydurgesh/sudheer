# Generated by Django 4.0.5 on 2022-10-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('flight_id', models.IntegerField()),
                ('seat_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('destination', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
                ('mail', models.EmailField(max_length=256)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
