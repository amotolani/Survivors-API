# Generated by Django 3.1.7 on 2021-06-16 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210617_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='parents_and_children',
            new_name='parentsOrChildrenAboard',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='pclass',
            new_name='passengerClass',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='siblings_and_spouses',
            new_name='siblingsOrSpousesAboard',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='id',
            new_name='uuid',
        ),
    ]
