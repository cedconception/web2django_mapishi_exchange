# Generated by Django 5.0.3 on 2024-05-26 13:56

import recipes.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0016_alter_recipe_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to="recipes/img/",
                validators=[recipes.models.validate_image],
            ),
        ),
    ]
