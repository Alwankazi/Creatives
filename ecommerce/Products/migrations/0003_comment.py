# Generated by Django 3.0 on 2020-10-13 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_auto_20201011_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('approved_comment', models.BooleanField(default=False)),
                ('parent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Products.Comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('view_reply', 'Can view comments reply.'), ('delete_reply', 'Can delete comments reply'), ('change_reply', 'Can change comments reply.'), ('create_reply', 'Can give reply to comments'), ('approve_reply', 'Can approve comments'), ('disapprove_reply', 'Can disapprove comments')],
            },
        ),
    ]
