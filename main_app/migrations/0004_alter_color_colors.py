# Generated by Django 4.1.1 on 2022-10-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_color_coat_pattern_color_colors_color_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='colors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='main_app.breed'),
        ),
    ]
