# Generated by Django 3.2.3 on 2021-05-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_songdetail_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdetail',
            name='song_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]