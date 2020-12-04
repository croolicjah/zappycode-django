# Generated by Django 3.1.1 on 2020-12-04 00:08

from django.db import migrations


def link_body_to_content(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')

    for post in Post.objects.all():
        post.content = post.body
        post.save()


def link_bonus_to_member_content(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')

    for post in Post.objects.all():
        post.member_content = post.bonus
        post.save()


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0007_auto_20201204_0002'),
    ]

    operations = [
        migrations.RunPython(link_body_to_content),
        migrations.RunPython(link_bonus_to_member_content),
    ]
