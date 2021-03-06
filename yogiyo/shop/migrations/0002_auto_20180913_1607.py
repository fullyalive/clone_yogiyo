# Generated by Django 2.1.1 on 2018-09-13 16:07

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='meta',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='shop',
            name='latlng',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shop',
            name='meta',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
