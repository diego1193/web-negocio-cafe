# Generated by Django 4.2.16 on 2024-09-14 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'sercicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
