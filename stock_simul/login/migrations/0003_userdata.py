# Generated by Django 5.0.6 on 2024-05-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('secPassword', models.CharField(max_length=30)),
            ],
        ),
    ]
