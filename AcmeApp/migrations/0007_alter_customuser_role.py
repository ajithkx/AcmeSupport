# Generated by Django 4.0.5 on 2022-06-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcmeApp', '0006_customuser_is_active_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=50),
        ),
    ]
