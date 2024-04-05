# Generated by Django 5.0.3 on 2024-03-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField(verbose_name='게시글 ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('writer', models.CharField(max_length=10, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
