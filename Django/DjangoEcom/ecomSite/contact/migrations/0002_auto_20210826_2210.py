# Generated by Django 3.2.6 on 2021-08-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=800)),
                ('location', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=800)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
    ]