# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models





class AppraisalRoles(models.Model):
    idappraisal_role = models.IntegerField(primary_key=True)
    role = models.CharField(unique=True, max_length=45)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'appraisal_roles'


class AppraisalroleAttributes(models.Model):
    idappraisalrole_attribute = models.IntegerField(db_column='idAppraisalRole_Attribute', primary_key=True)  # Field name made lowercase.
    idrole = models.ForeignKey(AppraisalRoles, db_column='idRole')  # Field name made lowercase.
    idattribute = models.ForeignKey('AttributesMaster', db_column='idAttribute')  # Field name made lowercase.
    weightage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'appraisalrole_attributes'


class AppraiserType(models.Model):
    idappraiser_type = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    idtype = models.IntegerField(db_column='idType')  # Field name made lowercase.
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'appraiser_type'


class AttributeAppraiserComments(models.Model):
    idattribute_appraiser_comments = models.IntegerField(primary_key=True)
    id_appraisal_role_attributes = models.ForeignKey(AppraisalroleAttributes, db_column='id_appraisal_role_attributes')
    id_employee = models.ForeignKey('Employee', db_column='id_employee',related_name='id_employee')
    id_comment_employee = models.ForeignKey('Employee', db_column='id_comment_employee')
    comments = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_appraiser_comments'


class AttributeRating(models.Model):
    idattribute_rating = models.IntegerField(primary_key=True)
    appraisee = models.ForeignKey('Employee', db_column='appraisee',related_name='appraisee')
    appraiser = models.ForeignKey('Employee', db_column='appraiser')
    id_attribute_role_appraiser = models.ForeignKey(AppraisalroleAttributes, db_column='id_attribute_role_appraiser', blank=True, null=True)
    id_employee_attribute = models.ForeignKey('EmployeeAttributes', db_column='id_employee_attribute', blank=True, null=True)
    appraiser_type = models.ForeignKey(AppraiserType, db_column='appraiser_type', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_rating'


class AttributesMaster(models.Model):
    idattributes_master = models.IntegerField(db_column='idATTRIBUTES_MASTER', primary_key=True)  # Field name made lowercase.
    attribute = models.CharField(max_length=300, blank=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'attributes_master'


class AuthGroup(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Break(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    id_timing = models.ForeignKey('Timing', db_column='id_timing')
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'break'


class DjangoAdminLog(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=45, blank=True)
    pan_id = models.CharField(unique=True, max_length=45, blank=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    skype_id = models.CharField(unique=True, max_length=45, blank=True)
    yahoo_id = models.CharField(unique=True, max_length=45, blank=True)
    email = models.CharField(unique=True, max_length=45, blank=True)
    account_enabled = models.TextField()  # This field type is a guess.
    current_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    projects_worked = models.CharField(max_length=100, blank=True)
    image_name = models.CharField(max_length=45, blank=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)
    sex = models.TextField(blank=True)  # This field type is a guess.
    colleges_attended = models.TextField(blank=True)
    worked_at = models.TextField(blank=True)
    date_joined = models.DateField(blank=True, null=True)
    languages_known = models.TextField(blank=True)
    appraisal_date = models.DateField()
    passport_number = models.CharField(unique=True, max_length=45, blank=True)
    beehyv_id = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.first_name)
    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeAppraisalRole(models.Model):
    idemployee_appraisal_role = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, blank=True, null=True)
    appraisal_role = models.ForeignKey(AppraisalRoles, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_appraisal_role'


class EmployeeAttributes(models.Model):
    idemployee_attributes = models.IntegerField(primary_key=True)
    id_employee = models.ForeignKey(Employee, db_column='id_employee')
    id_attributes_master = models.ForeignKey(AttributesMaster, db_column='id_attributes_master')
    weightage = models.IntegerField()
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'employee_attributes'


class EmployeeProject(models.Model):
    idemployee_project = models.IntegerField(primary_key=True)
    employee = models.ForeignKey(Employee, blank=True, null=True)
    project = models.ForeignKey('Project', blank=True, null=True)
    fromdate = models.DateField(db_column='fromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateField(db_column='toDate', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_byl = models.CharField(max_length=45, blank=True)
    employee_percentage_allocation = models.IntegerField(blank=True, null=True)
    billable_role = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employee_project'


class EmployeeRole(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    id_role = models.ForeignKey('Role', db_column='id_role')
    id_employee = models.ForeignKey(Employee, db_column='id_employee')
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'employee_role'


class EmployeeTechnologies(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    employee = models.ForeignKey(Employee)
    technology = models.ForeignKey('TechnologiesMaster')
    date_added = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_technologies'


class Extappraisers(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'extappraisers'


class Holiday(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.DateField(unique=True)
    description = models.CharField(max_length=45)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'holiday'


class Leave(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    employee = models.ForeignKey(Employee, blank=True, null=True,related_name='employee')
    approver_employee = models.ForeignKey(Employee, blank=True, null=True)
    leave_date = models.DateField()
    leave_type = models.CharField(max_length=245, blank=True)
    leave_status = models.CharField(max_length=245, blank=True)

    class Meta:
        managed = False
        db_table = 'leave'


class Phone(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    phone_number = models.CharField(max_length=45, blank=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    is_mobile = models.TextField()  # This field type is a guess.
    id_employee = models.ForeignKey(Employee, db_column='id_employee',related_name='id_employee_relatedname')
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Project(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    project_title = models.CharField(max_length=100)
    project_lead = models.ForeignKey(Employee, blank=True, null=True)
    project_description = models.TextField(blank=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)
    billability = models.TextField(blank=True)  # This field type is a guess.
    status = models.CharField(max_length=45, blank=True)
    def __str__(self):
        return str(self.project_title)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectExtappraisers(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    project = models.ForeignKey(Project)
    extappraisers = models.ForeignKey(Extappraisers)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'project_extappraisers'


class ProjectSupervisors(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'project_supervisors'


class Role(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    role = models.CharField(unique=True, max_length=45)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'role'


class Task(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    is_appraisable = models.TextField(blank=True)  # This field type is a guess.
    description = models.TextField(blank=True)
    hours = models.IntegerField(blank=True, null=True)
    isparent = models.TextField(db_column='isParent')  # Field name made lowercase. This field type is a guess.
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'task'


class TaskAppraisers(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    task = models.ForeignKey(Task)
    appraiser_rating = models.IntegerField(blank=True, null=True)
    appraiser = models.ForeignKey(Employee, blank=True, null=True)
    appraiser_type = models.ForeignKey(AppraiserType, db_column='appraiser_type', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)
    extappr = models.ForeignKey(Extappraisers, db_column='extAppr_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task_appraisers'


class TaskAttributes(models.Model):
    idtaskattribute = models.IntegerField(db_column='idtaskAttribute', primary_key=True)  # Field name made lowercase.
    idtask = models.ForeignKey(Task, db_column='idTask',related_name='idTask')  # Field name made lowercase.
    id_appraisal_role_attribute = models.ForeignKey(AppraisalroleAttributes, db_column='id_appraisal_role_attribute')
    id_employee = models.ForeignKey(Employee, db_column='id_employee')
    created_by = models.CharField(max_length=45, blank=True)
    create_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    id_task = models.ForeignKey(Task, db_column='id_task')

    class Meta:
        managed = False
        db_table = 'task_attributes'


class TaskComments(models.Model):
    idtask_comments = models.IntegerField(primary_key=True)
    id_task = models.ForeignKey(Task, db_column='id_task')
    id_employee = models.ForeignKey(Employee, db_column='id_employee')
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'task_comments'


class TaskDateTime(models.Model):
    tdt_id = models.IntegerField(primary_key=True)
    task = models.IntegerField()
    hours = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    updated_by = models.CharField(max_length=45, blank=True)
    task_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_date_time'


class TaskEffort(models.Model):
    tdt_id = models.IntegerField(primary_key=True)
    task = models.ForeignKey(Task, db_column='task', related_name='task_content_type')
    hours = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    updated_by = models.CharField(max_length=45, blank=True)
#     task_id = models.IntegerField( )
    wfh_hours = models.TimeField(db_column='WFH_hours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task_effort'


class TechnologiesMaster(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'technologies_master'


class Timing(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    in_time = models.DateTimeField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)
    id_employee = models.ForeignKey(Employee, db_column='id_employee', blank=True, null=True)
    date = models.DateField()
    is_leave = models.TextField(blank=True)  # This field type is a guess.
    leave_reason = models.CharField(max_length=245, blank=True)
    work_from_home = models.IntegerField(blank=True, null=True)
    wfh_description = models.CharField(max_length=245, blank=True)
    create_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=45, blank=True)
    total_time = models.TimeField(blank=True, null=True)
    breaks = models.TimeField(blank=True, null=True)
    tot_working = models.TimeField(blank=True, null=True)
    deficit = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timing'


class WeeklySubmittedReports(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    employee = models.ForeignKey(Employee)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    submitted_report = models.TextField(db_column='submitted_Report', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'weekly_submitted_reports'


class WeeklyTask(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.TextField()
    hours = models.IntegerField()
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project, blank=True, null=True)
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    task = models.ForeignKey(Task, blank=True, null=True)
    taskable = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'weekly_task'


class ExternalAppraiserUser(models.Model):
    idextuser=models.IntegerField()
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=32)
    email=models.EmailField(max_length=254)
class AdminUser(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=32)
    
class ExtraTaskAppraisers(models.Model):
    task = models.CharField(max_length=200)
    description=models.CharField(max_length=20000)
    appraiser_rating = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField( blank=True, null=True)
    project_id= models.IntegerField( blank=True, null=True)

class ExtraAttributesAppraiser(models.Model):
    attribute= models.CharField(max_length=200)
    weightage= models.IntegerField(blank=True, null=True)
    appraiser_rating = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField( blank=True, null=True)
    project_id= models.IntegerField( blank=True, null=True)

    