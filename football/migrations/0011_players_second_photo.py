# Generated by Django 4.1.3 on 2023-05-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0010_champions_league_scores_alter_player_matches_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='second_photo',
            field=models.ImageField(default='url', upload_to='photos/players/'),
        ),
    ]
