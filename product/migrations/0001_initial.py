# Generated by Django 3.0.3 on 2020-02-18 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'maincategories',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_cate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('alergy', models.CharField(max_length=100)),
                ('nutrition1', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nutrition2', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nutrition3', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nutrition4', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nutrition5', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nutrition6', models.DecimalField(decimal_places=1, max_digits=4)),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
                ('size_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
                ('sub_category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SubCategory')),
                ('theme_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Theme')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]