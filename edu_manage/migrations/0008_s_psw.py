# Generated by Django 2.0 on 2019-01-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_manage', '0007_auto_20190103_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='s',
            name='psw',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
