# Generated by Django 3.2.6 on 2024-10-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20241010_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
