# Generated by Django 2.1.3 on 2018-11-06 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('script_codes', '0002_script_codes_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='script',
            options={'ordering': ['code']},
        ),
    ]