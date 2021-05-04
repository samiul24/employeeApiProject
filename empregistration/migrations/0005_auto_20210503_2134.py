# Generated by Django 3.0.2 on 2021-05-03 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empregistration', '0004_auto_20210501_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empbasicinfo',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='empbasicinfo',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='empbasicinfo',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.EmpDepartment'),
        ),
        migrations.AlterField(
            model_name='empbasicinfo',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.EmpDesignation'),
        ),
        migrations.AlterField(
            model_name='empbasicinfo',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.District'),
        ),
        migrations.AlterField(
            model_name='empbasicinfo',
            name='thana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.Thana'),
        ),
        migrations.AlterField(
            model_name='empdepartment',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='empdesignation',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='empeducation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.EmpBasicInfo'),
        ),
        migrations.AlterField(
            model_name='empsalary',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.EmpBasicInfo'),
        ),
        migrations.AlterField(
            model_name='thana',
            name='thana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empregistration.District'),
        ),
    ]