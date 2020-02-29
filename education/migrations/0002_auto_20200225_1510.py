# Generated by Django 2.2.10 on 2020-02-25 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'professor_user': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.ManyToManyField(blank=True, limit_choices_to={'professor_user': True}, related_name='course_p', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, limit_choices_to={'student_user': True}, related_name='course_s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(limit_choices_to={'student_user': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='author',
            field=models.ForeignKey(limit_choices_to={'professor_user': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
