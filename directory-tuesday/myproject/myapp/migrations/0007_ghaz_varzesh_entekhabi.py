from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_ghaz'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghaz',
            name='varzesh_ENTEKHABI',
            field=models.CharField(choices=[('1', 'BODYCOMBAT'), ('2', 'BODYPUMP'), ('3', 'FUNCTIONAL')], default='3', max_length=1),
        ),
    ]
