# Generated by Django 4.1.3 on 2022-12-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountVehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, max_length=255, upload_to='videos/')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
