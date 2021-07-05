# Generated by Django 3.1.7 on 2021-06-16 23:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pclass', models.PositiveSmallIntegerField(choices=[(1, 'First Class'), (2, 'Second Class'), (3, 'Third Class')], default=False)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NON-BINARY', 'Non-Binary'), ('TRANSGENDER', 'Transgender')], max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('siblings_and_spouses', models.PositiveSmallIntegerField(blank=True)),
                ('parents_and_children', models.PositiveSmallIntegerField(blank=True)),
                ('survived', models.BooleanField()),
                ('fare', models.FloatField()),
            ],
            options={
                'db_table': 'api',
            },
        ),
    ]
