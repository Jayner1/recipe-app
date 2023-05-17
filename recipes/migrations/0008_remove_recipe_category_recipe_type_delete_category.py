# Generated by Django 4.2 on 2023-05-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Breakfasts', 'Breakfasts'), ('Lunches', 'Lunches'), ('Dinners', 'Dinners')], default='Breakfasts', max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
