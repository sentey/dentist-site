# Generated by Django 4.1.4 on 2023-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_appointment_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
