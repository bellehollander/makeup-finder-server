# Generated by Django 4.2.5 on 2023-09-07 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MakeupPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MakeupSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('makeup_preferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.makeuppreferences')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('makeup_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.makeupskill')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('makeup_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.makeupskill')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MakeupPreferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.makeuppreferences')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.profile')),
            ],
        ),
        migrations.AddField(
            model_name='makeuppreferences',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeupapi.producttype'),
        ),
    ]
