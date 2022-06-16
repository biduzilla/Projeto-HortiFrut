# Generated by Django 3.2.12 on 2022-06-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220614_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='latidude',
        ),
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=256, null=True),
        ),
    ]