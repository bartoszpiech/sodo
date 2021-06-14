# Generated by Django 3.2 on 2021-06-14 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='database.room'),
        ),
    ]