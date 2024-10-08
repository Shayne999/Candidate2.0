# Generated by Django 5.1.1 on 2024-09-19 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaleinformation',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_info', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='career',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='recruiterprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruiter_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='references',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='references', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='core.cv'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_experience', to='core.cv'),
        ),
    ]
