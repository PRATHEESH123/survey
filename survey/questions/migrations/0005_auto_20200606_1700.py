# Generated by Django 2.2.7 on 2020-06-06 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_multiplechoiceanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choiceanswer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Choice'),
        ),
    ]