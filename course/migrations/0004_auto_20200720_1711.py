# Generated by Django 3.0.8 on 2020-07-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_personaltrainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaltrainer',
            name='course',
        ),
        migrations.RemoveField(
            model_name='personaltrainer',
            name='price',
        ),
        migrations.CreateModel(
            name='PersonalTrainerCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, verbose_name="Prezzo dell'istruttore")),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
                ('personalTrainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.PersonalTrainer')),
            ],
        ),
    ]
