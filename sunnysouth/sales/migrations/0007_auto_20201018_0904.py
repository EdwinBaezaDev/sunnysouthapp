# Generated by Django 3.1 on 2020-10-18 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20201012_0509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'get_latest_by': 'created', 'ordering': ['-created', '-modified']},
        ),
    ]
