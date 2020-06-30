# Generated by Django 3.0.7 on 2020-06-21 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200528_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenotation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]
