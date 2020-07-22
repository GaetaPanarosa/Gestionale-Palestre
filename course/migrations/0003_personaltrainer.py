# Generated by Django 3.0.8 on 2020-07-20 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer', '0002_auto_20200720_1654'),
        ('course', '0002_auto_20200716_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalTrainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, verbose_name="Prezzo dell'istruttore")),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trainer.Trainer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
