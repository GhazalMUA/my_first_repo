# Generated by Django 5.0 on 2023-12-15 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_restaurantmenu_dastebandi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmenu',
            name='dastebandi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.dastebandi'),
        ),
    ]
