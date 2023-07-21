# Generated by Django 4.2.1 on 2023-07-19 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_alter_book_isbn_alter_book_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reserved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='reserved_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
