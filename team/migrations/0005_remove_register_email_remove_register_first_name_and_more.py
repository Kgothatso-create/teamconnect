# Generated by Django 4.2 on 2023-07-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_register_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.AddField(
            model_name='register',
            name='message',
            field=models.TextField(default='', max_length=550),
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
