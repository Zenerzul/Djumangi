# Generated by Django 3.1.2 on 2020-10-17 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=100)),
                ('employee_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('skills', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=32)),
                ('salary_from', models.IntegerField()),
                ('salary_to', models.IntegerField()),
                ('posted', models.DateField(max_length=32)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                          related_name='vacancies', to='job_offer.specialty')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='vacancies', to='job_offer.company')),
            ],
        ),
    ]
