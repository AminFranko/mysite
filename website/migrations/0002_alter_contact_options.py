# Generated by Django 3.2.10 on 2021-12-16 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('created_date',)},
        ),
    ]
