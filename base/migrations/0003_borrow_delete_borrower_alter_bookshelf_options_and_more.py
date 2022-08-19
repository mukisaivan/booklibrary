# Generated by Django 4.0.6 on 2022-08-19 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_bookshelf_borrowers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_time', models.DateTimeField(auto_now_add=True)),
                ('return_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Borrower',
        ),
        migrations.AlterModelOptions(
            name='bookshelf',
            options={'ordering': ['-borrow_time', '-return_time']},
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='borrow_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='return_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='borrow',
            name='bookshelf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.bookshelf'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
