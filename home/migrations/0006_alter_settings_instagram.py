# Generated by Django 5.0.2 on 2024-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_settings_facebook_alter_settings_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.URLField(default='instagram', max_length=150),
        ),
    ]