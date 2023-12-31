# Generated by Django 4.2.5 on 2023-09-14 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MediaManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('shortname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('created', models.DateField(verbose_name='Ստեղծման Տարի')),
            ],
        ),
        migrations.CreateModel(
            name='PointType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=25)),
                ('works_since', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='WorkerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.IntegerField()),
                ('lessons', models.IntegerField(verbose_name='Սեմեստրի լեկցիաների քանակը')),
                ('lecturers', models.ManyToManyField(to='university.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=36)),
                ('last_name', models.CharField(max_length=72)),
                ('surname', models.CharField(max_length=36)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('joined', models.DateField()),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('state_order', models.BooleanField(default=False)),
                ('tuition_fee', models.IntegerField(default=0)),
                ('phone', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.group')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                            to='MediaManagement.image')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.workertype'),
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('years', models.IntegerField()),
                ('remote', models.BooleanField(blank=True, default=False, verbose_name='հեռակա')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.faculty')),
                ('subjects', models.ManyToManyField(to='university.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.student')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.pointtype')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='lecturers',
            field=models.ManyToManyField(to='university.staff'),
        ),
        migrations.AddField(
            model_name='group',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.profession'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='dean',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='university.staff'),
        ),
        migrations.AddField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.group'),
        ),
        migrations.AddField(
            model_name='exam',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='university.staff'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.examtype'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('shortname', models.CharField(max_length=50)),
                ('manager',
                 models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='department',
                                      to='university.staff')),
                ('teachers', models.ManyToManyField(related_name='departments', to='university.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Deferral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(verbose_name='Տարկետման սեմեստր')),
                ('length', models.IntegerField(verbose_name='Ժամկետ')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.student')),
            ],
        ),
        migrations.CreateModel(
            name='AbsenceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loose', models.BooleanField(default=True)),
                ('minute', models.IntegerField()),
                ('date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.group')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.student')),
            ],
        ),
    ]
