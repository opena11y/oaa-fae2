# Generated by Django 2.2.7 on 2019-12-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuleCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_category_code', models.IntegerField(unique=True)),
                ('category_id', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('title_plural', models.CharField(max_length=256, verbose_name='Title Plural')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=32)),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Rule Category',
                'verbose_name_plural': 'Rule Categories',
                'ordering': ['order', 'title'],
            },
        ),
    ]
