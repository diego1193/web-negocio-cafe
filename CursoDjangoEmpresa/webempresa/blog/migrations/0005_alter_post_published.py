# Generated by Django 4.2.16 on 2024-09-14 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 14, 23, 0, 8, 195918, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]
