# Generated by Django 5.0.3 on 2024-04-09 09:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='코멘트를 작성할 게시글'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DIARY', '일기'), ('STUDY', '공부'), ('ETC', '기타')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
