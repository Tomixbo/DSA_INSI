# Generated by Django 5.0.4 on 2024-05-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0011_alter_performance_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="performance",
            name="description",
            field=models.CharField(max_length=150),
        ),
    ]
