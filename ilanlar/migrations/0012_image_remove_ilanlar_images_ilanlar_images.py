# Generated by Django 5.0.2 on 2024-03-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilanlar', '0011_delete_ilanresimleri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='ilanlar',
            name='images',
        ),
        migrations.AddField(
            model_name='ilanlar',
            name='images',
            field=models.ManyToManyField(blank=True, to='ilanlar.image'),
        ),
    ]
