# Generated by Django 3.1.4 on 2021-01-21 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20210120_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]
