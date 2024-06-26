# Generated by Django 5.0.3 on 2024-04-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_version_version_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('number',), 'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.RenameField(
            model_name='version',
            old_name='version_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='version_number',
            new_name='number',
        ),
    ]
