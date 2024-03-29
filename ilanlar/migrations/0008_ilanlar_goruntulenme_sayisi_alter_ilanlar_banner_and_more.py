# Generated by Django 5.0.2 on 2024-03-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilanlar', '0007_alter_ilanlar_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilanlar',
            name='goruntulenme_sayisi',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='ilanlar',
            name='banner',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ilanlar',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ilanlar',
            name='km',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ilanlar',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ilanlar',
            name='status',
            field=models.CharField(choices=[('True', 'Aktif'), ('False', 'Deaktif')], default='True', max_length=10),
        ),
    ]
