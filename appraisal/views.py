from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login,logout
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.core.context_processors import csrf
from appraisal.models import EmployeeAppraisalRole,AppraisalroleAttributes,ExtraTaskAppraisers,ExtraAttributesAppraiser
from appraisal.models import Extappraisers,ExternalAppraiserUser,ProjectExtappraisers,Task,AttributesMaster,EmployeeProject,Employee
from django.template import RequestContext
from django.http import JsonResponse
import json
from django.core import serializers
from django.contrib import messages 


#the decorator
def myuser_login_required(f):
        def wrap(request, *args, **kwargs):
                #this check the session if user key exist, if not it will redirect to login page
                if 'user' not in request.session.keys():
                    return HttpResponseRedirect("../appraiserlogin")
                return f(request, *args, **kwargs)
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__
        return wrap
def user_login_required(f):
        def wrap(request, *args, **kwargs):
                #this check the session if user key exist, if not it will redirect to login page
                if 'user' not in request.session.keys():
                    return HttpResponseRedirect("../login")
                return f(request, *args, **kwargs)
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__
        return wrap

def admin_login(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_active: 
                request.session['user']=user.is_active                                
                login(request,user)
                return  HttpResponseRedirect('../home')
            else:
                c['s']="Deleted Account"
        else:
            c['s']="Username or password incorrect"
    return render_to_response("login.html", c)
def logout_view_admin(request):
    logout(request)
    return redirect('../login')
def logout_view_appraiser(request):
    logout(request)
    return redirect('appraiserlogin')
@user_login_required
def home(request):
    msg=''
    if request.POST:
        id=request.POST.get('appraisers')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if id and username and password:
            if len(ExternalAppraiserUser.objects.filter(username=username)) >0:
                msg +="Username already Exist, Please create another username" 
            else:          
                t=ExternalAppraiserUser.objects.create(idextuser=id,username=username,email=email,password=password)
                t.save()
                return HttpResponseRedirect("../success")
        else:
            msg +="Please fill all the required field"
    x=Extappraisers.objects.all()
    appraiser=[]
    for a in x:
        d={}
        d['first_name']=a.first_name
        x=a.last_name
        if x == None:
            d['last_name']=''
        else:
            d['last_name']=x
            
        d['id']=a.id
        appraiser.append(d)
    return render_to_response("home.html",{'appraiser':appraiser,'msg':msg}, RequestContext(request))

def success(request):
    return render_to_response("success.html",{})
def appraiserlogin(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        uname=request.POST.get('username') 
        pwd=request.POST.get('password')
        if uname and pwd:
            user = ExternalAppraiserUser.objects.values_list('username').filter(username=uname)
            password=ExternalAppraiserUser.objects.values_list('password').filter(username=uname) 
            if len(user) >0:
                request.session['user'] = user[0]
                if password[0][0] == pwd and user[0][0]==uname:  
                    url = reverse('appraiserhome', kwargs={ 'username': uname })                             
                    return  HttpResponseRedirect(url)
                else:
                    c['s']=" username or Password is incorrect, Please try again with correct password"
            else:
                c['s']="Username is incorrect,Please try again with correct username"
        else:
            c['s']="Please enter username and password"
    return render_to_response("login.html", c)


@myuser_login_required   
def appraiserhome(request,*args,**kwargs):
    name_extapp=kwargs['username']
    print name_extapp
    app_ext_id=ExternalAppraiserUser.objects.values_list('idextuser').filter(username=name_extapp)
    project_id=ProjectExtappraisers.objects.values_list('project_id').filter(extappraisers_id=app_ext_id)
    emp_id=EmployeeProject.objects.values_list('employee_id').filter(project_id=project_id)
    emp_dict=Employee.objects.values_list().filter(id__in=emp_id)
    empl_dict=[]
    pid=project_id[0][0]
    msg=""
    for i in emp_dict:
        x={}
        x['id']=i[0]
        x['name']=i[1]
        test=ExtraTaskAppraisers.objects.filter(project_id=pid,employee_id=i[0])
        if len(test)==0:
            empl_dict.append(x)
    if request.POST:
        title=request.POST.getlist('title')
        description=request.POST.getlist('description')
        rating=request.POST.getlist('ratings')
        employee_id=request.POST.get('employees') 
        length=len(title)
        if len(rating)==length:
            for i in range(length):
                z=ExtraTaskAppraisers.objects.create()
                z.task=title[i]
                z.description=description[i]
                if rating[i]=="Select Rating":
                    z.appraiser_rating=0
                else:
                    z.appraiser_rating=rating[i]
                z.project_id=project_id[0][0]
                z.employee_id=employee_id   
                z.save()
            url = reverse('success_appraiser', kwargs={'uname': name_extapp})
            return redirect(url)
        else:
            msg+= "Please select all the ratings "
        
#         
    return render_to_response("extappraiser.html",{"name_extapp":name_extapp,"emp_dict":empl_dict,"msg":msg},RequestContext(request))

@myuser_login_required
def app_role(request,*args,**kwargs):
    name_extapp=kwargs['uname']
    app_ext_id=ExternalAppraiserUser.objects.values_list('idextuser').filter(username=name_extapp)
    project_id=ProjectExtappraisers.objects.values_list('project_id').filter(extappraisers_id=app_ext_id)
    emp_id=EmployeeProject.objects.values_list('employee_id').filter(project_id=project_id)
    emp_dict=Employee.objects.values_list().filter(id__in=emp_id)
    empl_dict=[]
    for i in emp_dict:
        x={}
        x['id']=i[0]
        x['name']=i[1]
        empl_dict.append(x)
    if request.POST:
        attribute=request.POST.getlist('attribute')
        print attribute
        weightage=request.POST.getlist('weightage')
        rating=request.POST.getlist('ratings')
        employee_id=request.POST.get('employees') 
        length=len(attribute)
        for i in range(length):
            z=ExtraAttributesAppraiser.objects.create()
            z.attribute=attribute[i]
            z.weightage=weightage[i]
            if rating[i]=="Select Rating":
                z.appraiser_rating=0
            else:
                z.appraiser_rating=rating[i]
            z.employee_id=employee_id
            z.project_id=project_id[0][0]
            z.save()
        url = reverse('success_app_role', kwargs={'uname': name_extapp})
        return redirect(url)

        
    return render_to_response("attributes.html",{"name_extapp":name_extapp,"emp_dict":empl_dict},RequestContext(request))

@myuser_login_required
def appraiser(request,*args,**kwargs):
    name_extapp=kwargs['uname']
    app_ext_id=ExternalAppraiserUser.objects.values_list('idextuser').filter(username=name_extapp)
    project_id=ProjectExtappraisers.objects.values_list('project_id').filter(extappraisers_id=app_ext_id)
    if request.POST:
        emp_id=request.POST.get('id')
        tasks=Task.objects.values_list().filter(employee_id=emp_id,project_id=project_id)
        objs_app=[]
        for a in tasks:
            x={}
            x['title']=a[3]
            x['description']=a[8]
            objs_app.append(x)           

    return JsonResponse(objs_app,safe=False)

@myuser_login_required
def app_role_select(request,*args,**kwargs):
    app_objs=[]
    
    if request.POST:
        emp_id=request.POST.get('id')
        appraisal_role_id=EmployeeAppraisalRole.objects.values_list('appraisal_role_id').filter(employee_id=emp_id)
        attribute_id=AppraisalroleAttributes.objects.values_list('idattribute').filter(idrole=appraisal_role_id)
        attribute_ids=[]
        for i in attribute_id:
            attribute_ids.append(i[0])
        attributes=AttributesMaster.objects.values_list('attribute').filter(idattributes_master__in=attribute_id)
        attribute=[]
        for i in attributes:
            attribute.append(i[0])
            
        weightage=AppraisalroleAttributes.objects.values_list('weightage').filter(idrole=appraisal_role_id)
        weightages=[]
        for i in weightage:
            weightages.append(i[0])            
        for i in range(len(attribute)):
            x={}
            x['id']=attribute_ids[i]
            x['attribute']=attribute[i]
            x['weightage']=weightages[i]
            app_objs.append(x)
    return JsonResponse(app_objs,safe=False)
@myuser_login_required
def success_appraiser(request,*args,**kwargs):
    name_extapp=kwargs['uname']
    print name_extapp
    return render(request, "success_rate_another_employee.html", { "name":name_extapp })
@myuser_login_required
def success_app_role(request,*args,**kwargs):
    name_extapp=kwargs['uname']
    print name_extapp
    return render(request, "success_rate_another.html", { "name":name_extapp })
@myuser_login_required
def help(request,*args,**kwargs):
    name_extapp=kwargs['uname']
    return render_to_response("help.html",{'name_extapp':name_extapp})   