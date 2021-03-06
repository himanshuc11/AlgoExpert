# Generated by Django 4.0.1 on 2022-01-20 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_problemlist_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algoexpertuser',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='algoexpertuser',
            name='solution',
        ),
        migrations.CreateModel(
            name='AlgoExpertUserSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_submission', to='problems.problemlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.algoexpertuser')),
            ],
        ),
    ]
