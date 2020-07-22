# Generated by Django 3.0.8 on 2020-07-14 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Corso')),
                ('description', models.CharField(max_length=5000, null=True, verbose_name='Descrizione')),
                ('min_subscribers', models.IntegerField(default=0, verbose_name='Numero minimo iscritti')),
                ('max_subscribers', models.IntegerField(default=0, verbose_name='Numero massimo iscritti')),
                ('price',
                 models.DecimalField(decimal_places=1, default=0, max_digits=9, null=True, verbose_name='Prezzo')),
                ('active', models.BooleanField(default=True, verbose_name='Attivo')),
                ('start_date', models.DateField(null=True, verbose_name='Data inizio corso')),
                ('end_date', models.DateField(null=True, verbose_name='Data fine corso')),
                ('n_max_prenotation', models.IntegerField(verbose_name='Numero di posti')),
                ('trainer',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trainer.Trainer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CourseDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(
                    choices=[(0, 'Lunedi'), (1, 'Martedi'), (2, 'Mercoledì'), (3, 'Giovedì'), (4, 'Venerdì'),
                             (5, 'Sabato'), (6, 'Domenica')])),
                ('active', models.BooleanField(default=True)),
                ('course',
                 models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DisactiveCourseOnDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Giorno da disattivare')),
                ('active', models.BooleanField(default=False)),
                ('course',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
                ('dateRange',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.DateRange')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_dismiss_hour', models.IntegerField(verbose_name='Tempo di disdetta in ore')),
                ('time_dismiss_minutes', models.IntegerField(verbose_name='Tempo di disdetta in minuti')),
                ('time_dismiss_secondi', models.IntegerField(verbose_name='Tempo di disdetta in secondi')),
                ('time_prenotation_hour', models.IntegerField(verbose_name='Tempo di prenotazione in ore')),
                ('time_prenotation_minutes', models.IntegerField(verbose_name='Tempo di prenotazione in minuti')),
                ('time_prenotation_secondi', models.IntegerField(verbose_name='Tempo di prenotazione in secondi')),
                ('course',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDayHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('coursedayhours',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.CourseDay')),
                (
                'hours', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Hours')),
            ],
        ),
    ]
