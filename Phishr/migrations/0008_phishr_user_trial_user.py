# Generated by Django 2.0.5 on 2018-05-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phishr', '0007_new_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='phishr_user',
            name='trial_user',
            field=models.BooleanField(default=True),
        ),
    ]
