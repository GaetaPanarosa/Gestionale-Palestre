# Generated by Django 3.0.8 on 2020-07-16 22:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='Immagine')),
                ('active', models.BooleanField(default=True, verbose_name='Attivo')),
            ],
        ),
    ]
