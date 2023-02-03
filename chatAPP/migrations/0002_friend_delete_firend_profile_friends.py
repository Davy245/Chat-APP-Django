# Generated by Django 4.1.6 on 2023-02-03 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chatAPP.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Firend',
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='chatAPP.friend'),
        ),
    ]
