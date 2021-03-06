# Generated by Django 2.2.3 on 2019-08-02 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField(max_length=10)),
                ('comment', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
