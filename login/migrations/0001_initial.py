# Generated by Django 4.2.4 on 2023-08-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('phoneno', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]