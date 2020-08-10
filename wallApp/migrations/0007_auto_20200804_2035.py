# Generated by Django 3.0.8 on 2020-08-05 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallApp', '0006_auto_20200804_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comm_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]