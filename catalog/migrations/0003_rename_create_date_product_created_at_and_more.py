# Generated by Django 5.0.3 on 2024-03-13 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='change_date',
            new_name='updated_at',
        ),
    ]