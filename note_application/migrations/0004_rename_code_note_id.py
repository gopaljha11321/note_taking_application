# Generated by Django 4.2.4 on 2024-02-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note_application', '0003_rename_id_note_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='code',
            new_name='id',
        ),
    ]
