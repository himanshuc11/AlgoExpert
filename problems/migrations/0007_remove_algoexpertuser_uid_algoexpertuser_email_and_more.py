# Generated by Django 4.0.1 on 2022-01-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_remove_algoexpertuser_problem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algoexpertuser',
            name='uid',
        ),
        migrations.AddField(
            model_name='algoexpertuser',
            name='email',
            field=models.EmailField(default='bac@gmail.com', max_length=2048, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='algoexpertuser',
            name='tier',
            field=models.CharField(choices=[('F', 'FREE'), ('P', 'PAID')], default='F', max_length=16),
        ),
    ]
