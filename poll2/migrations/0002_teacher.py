# Generated by Django 2.1.8 on 2019-06-13 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('detail', models.CharField(max_length=1023, verbose_name='详情')),
                ('good_count', models.IntegerField(verbose_name='好评数')),
                ('bad_count', models.IntegerField(verbose_name='差评数')),
                ('subject', models.ForeignKey(db_column='sno', on_delete=django.db.models.deletion.PROTECT, to='poll2.Subject', verbose_name='所属学科')),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'tb_teacher',
            },
        ),
    ]