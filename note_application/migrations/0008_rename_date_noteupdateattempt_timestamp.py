# Generated by Django 4.2.4 on 2024-02-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note_application', '0007_noteupdateattempt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noteupdateattempt',
            old_name='date',
            new_name='timestamp',
        ),
    ]
