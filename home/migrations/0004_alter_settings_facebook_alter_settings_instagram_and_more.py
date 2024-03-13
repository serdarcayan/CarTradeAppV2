# Generated by Django 5.0.2 on 2024-03-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_settings_linkedin_alter_settings_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.SlugField(default='facebook', max_length=150),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.SlugField(default='instagram', max_length=150),
        ),
        migrations.AlterField(
            model_name='settings',
            name='linkedin',
            field=models.SlugField(default='linkedin', max_length=150),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.SlugField(default='twitter', max_length=150),
        ),
    ]