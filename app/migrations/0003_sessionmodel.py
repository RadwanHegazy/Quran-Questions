# Generated by Django 4.0 on 2023-08-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_remove_surah_surah_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('uuid', models.CharField(max_length=10000)),
                ('answers', models.CharField(default='', max_length=1000)),
                ('correct_answer', models.CharField(max_length=1000)),
                ('user_answer', models.CharField(default='', max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]