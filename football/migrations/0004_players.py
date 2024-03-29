# Generated by Django 4.1.3 on 2022-12-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_scores_first_team_icon_scores_second_team_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateTimeField()),
                ('nationality', models.CharField(max_length=30)),
                ('current_team', models.CharField(max_length=30)),
                ('match_id', models.IntegerField()),
                ('first_team', models.CharField(max_length=30)),
                ('first_team_icon', models.URLField(default='null')),
                ('second_team', models.CharField(max_length=30)),
                ('second_team_icon', models.URLField(default='null')),
                ('match_date', models.DateTimeField()),
                ('score_first_team', models.IntegerField(default=0)),
                ('score_second_team', models.IntegerField(default=0)),
            ],
        ),
    ]
