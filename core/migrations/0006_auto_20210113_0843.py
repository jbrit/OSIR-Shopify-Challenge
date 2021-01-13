# Generated by Django 3.1.5 on 2021-01-13 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210113_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageitem',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='imageitem',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]