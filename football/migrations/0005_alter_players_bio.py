# Generated by Django 4.1.3 on 2022-12-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
