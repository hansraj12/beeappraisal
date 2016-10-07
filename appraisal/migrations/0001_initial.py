# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppraisalroleAttributes',
            fields=[
                ('idappraisalrole_attribute', models.IntegerField(db_column='idAppraisalRole_Attribute', primary_key=True, serialize=False)),
                ('weightage', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'appraisalrole_attributes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppraisalRoles',
            fields=[
                ('idappraisal_role', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=45, unique=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'appraisal_roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppraiserType',
            fields=[
                ('idappraiser_type', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('idtype', models.IntegerField(db_column='idType')),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'appraiser_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeAppraiserComments',
            fields=[
                ('idattribute_appraiser_comments', models.IntegerField(primary_key=True, serialize=False)),
                ('comments', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('last_update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attribute_appraiser_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeRating',
            fields=[
                ('idattribute_rating', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('last_update_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attribute_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttributesMaster',
            fields=[
                ('idattributes_master', models.IntegerField(db_column='idATTRIBUTES_MASTER', primary_key=True, serialize=False)),
                ('attribute', models.CharField(blank=True, max_length=300)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'attributes_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Break',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'break',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(blank=True, max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(blank=True, max_length=45)),
                ('pan_id', models.CharField(blank=True, max_length=45, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('skype_id', models.CharField(blank=True, max_length=45, unique=True)),
                ('yahoo_id', models.CharField(blank=True, max_length=45, unique=True)),
                ('email', models.CharField(blank=True, max_length=45, unique=True)),
                ('account_enabled', models.TextField()),
                ('current_address', models.TextField(blank=True)),
                ('permanent_address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('projects_worked', models.CharField(blank=True, max_length=100)),
                ('image_name', models.CharField(blank=True, max_length=45)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
                ('sex', models.TextField(blank=True)),
                ('colleges_attended', models.TextField(blank=True)),
                ('worked_at', models.TextField(blank=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
                ('languages_known', models.TextField(blank=True)),
                ('appraisal_date', models.DateField()),
                ('passport_number', models.CharField(blank=True, max_length=45, unique=True)),
                ('beehyv_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeAppraisalRole',
            fields=[
                ('idemployee_appraisal_role', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'employee_appraisal_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeAttributes',
            fields=[
                ('idemployee_attributes', models.IntegerField(primary_key=True, serialize=False)),
                ('weightage', models.IntegerField()),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'employee_attributes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('idemployee_project', models.IntegerField(primary_key=True, serialize=False)),
                ('fromdate', models.DateField(blank=True, db_column='fromDate', null=True)),
                ('todate', models.DateField(blank=True, db_column='toDate', null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_byl', models.CharField(blank=True, max_length=45)),
                ('employee_percentage_allocation', models.IntegerField(blank=True, null=True)),
                ('billable_role', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'employee_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'employee_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeTechnologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee_technologies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extappraisers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(blank=True, max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'extappraisers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('description', models.CharField(max_length=45)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'holiday',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField()),
                ('leave_type', models.CharField(blank=True, max_length=245)),
                ('leave_status', models.CharField(blank=True, max_length=245)),
            ],
            options={
                'db_table': 'leave',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=45)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('is_mobile', models.TextField()),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'phone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('project_description', models.TextField(blank=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
                ('billability', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectExtappraisers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'project_extappraisers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectSupervisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'project_supervisors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=45, unique=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('is_appraisable', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('hours', models.IntegerField(blank=True, null=True)),
                ('isparent', models.TextField(db_column='isParent')),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskAppraisers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appraiser_rating', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'task_appraisers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskAttributes',
            fields=[
                ('idtaskattribute', models.IntegerField(db_column='idtaskAttribute', primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'task_attributes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('idtask_comments', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'task_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskDateTime',
            fields=[
                ('tdt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('task', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_date', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('updated_by', models.CharField(blank=True, max_length=45)),
                ('task_id', models.IntegerField()),
            ],
            options={
                'db_table': 'task_date_time',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskEffort',
            fields=[
                ('tdt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hours', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_date', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('updated_by', models.CharField(blank=True, max_length=45)),
                ('wfh_hours', models.TimeField(blank=True, db_column='WFH_hours', null=True)),
            ],
            options={
                'db_table': 'task_effort',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TechnologiesMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'db_table': 'technologies_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField(blank=True, null=True)),
                ('out_time', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField()),
                ('is_leave', models.TextField(blank=True)),
                ('leave_reason', models.CharField(blank=True, max_length=245)),
                ('work_from_home', models.IntegerField(blank=True, null=True)),
                ('wfh_description', models.CharField(blank=True, max_length=245)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=45)),
                ('total_time', models.TimeField(blank=True, null=True)),
                ('breaks', models.TimeField(blank=True, null=True)),
                ('tot_working', models.TimeField(blank=True, null=True)),
                ('deficit', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'timing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeeklySubmittedReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('submitted_report', models.TextField(blank=True, db_column='submitted_Report')),
            ],
            options={
                'db_table': 'weekly_submitted_reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeeklyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('hours', models.IntegerField()),
                ('week_start_date', models.DateField()),
                ('week_end_date', models.DateField()),
                ('taskable', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'weekly_task',
                'managed': False,
            },
        ),
    ]
