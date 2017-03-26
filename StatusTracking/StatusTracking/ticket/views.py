from django.shortcuts import render
from django.contrib.auth import authenticate
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json as simplejson
from django.core.mail import EmailMessage

from django.contrib.auth.models import User
from .models import ICRequest, ScopeSupply, ServiceCall, ProductModel, Customer, EndUser

# Create your views here.
def index(request):
    if 'logged_in' in request.session:
        return render(request,'ticket/pages/profile.html')
    else:
        return render(request,'ticket/pages/login.html')

def login(request):
    return render(request,'ticket/pages/login.html')

def profile(request):
	if 'logged_in' in request.session:
    	 return render(request,'ticket/pages/profile.html')
	if request.method == 'POST':
		u = request.POST['user']
		p = request.POST['pass']
		user1 = authenticate(username=u, password=p)
		if user1 is not None:
			request.session['logged_in'] = u
			return render(request,'ticket/pages/profile.html')
		else:
    		 return render(request,'ticket/pages/login.html',{'error': 'Incorrect Username/Password'})

def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
        return render(request,'ticket/pages/login.html', {'error': 'Logged out'})
    else:
        return render(request, 'ticket/pages/login.html')
		
def ic_request(request):
	customer = Customer.objects.all()
	end_user = EndUser.objects.all()
	return render(request,'ticket/pages/ic_request.html',{'customer':customer, 'end_user':end_user})

def service_call(request):
	customer = Customer.objects.all()
	end_user = EndUser.objects.all()
	return render(request,'ticket/pages/service_call.html',{'customer':customer, 'end_user':end_user})
	
def scope_of_supply(request):
	if request.method == 'POST':
		customer = request.POST['customer']
		enduser = request.POST['enduser']
		sitename = request.POST['sitename']
		siteaddress = request.POST['siteaddress']
		contactpersonname1 = request.POST['contactpersonname1']
		contactpersonno1 = request.POST['contactpersonno1']
		contactpersonname2 = request.POST['contactpersonname2']
		contactpersonno2 = request.POST['contactpersonno2']
		reqdateinstall = request.POST['reqdateinstall']
		presignoff = request.POST['presignoff']
		sitestatus = request.POST['sitestatus']
		noofjobs = request.POST['noofjobs']
		nameofproduct = request.POST['nameofproduct']
		qty = request.POST['qty']
		transformervalvesize = request.POST['transformervalvesize']
		materialreached = request.POST['materialreached']
		salesmanagerrequestno = request.POST['salesmanagerrequestno']
		date = datetime.date.today()
		user = User.objects.get(username=request.session['logged_in'])
		ic = ICRequest(customer=customer,end_user=enduser,site_name=sitename,site_address=siteaddress,contact_person_name1=contactpersonname1,
		contact_person_no1=contactpersonno1,contact_person_name2=contactpersonname2,
		contact_person_no2=contactpersonno2,req_date_of_installation_by_customer=reqdateinstall,pre_sign_off_sheet_status=presignoff,
		site_status=sitestatus,no_of_jobs=noofjobs,name_of_product_supplied=nameofproduct
		,quantity=qty,transformer_valve_size_details=transformervalvesize,material_reached_at_site=materialreached,
		sales_manager_request_no=salesmanagerrequestno,date=date,created_by=user)
		ic.save()
		request.session['icrequestno'] = ic.id

	return render(request,'ticket/pages/scope_of_supply.html')
	
def product_model(request):
	if request.method == 'POST':
		customer = request.POST['customer']
		enduser = request.POST['enduser']
		sitename = request.POST['sitename']
		siteaddress = request.POST['siteaddress']
		contactpersonname1 = request.POST['contactpersonname1']
		contactpersonno1 = request.POST['contactpersonno1']
		contactpersonname2 = request.POST['contactpersonname2']
		contactpersonno2 = request.POST['contactpersonno2']
		reqdateinstall = request.POST['reqdateinstall']
		nameofproduct = request.POST['nameofproduct']
		cust_prob = request.POST['cust_prob']
		transformervalvesize = request.POST['transformervalvesize']
		date = datetime.date.today()
		salesmanagerrequestno = request.POST['salesmanagerrequestno']
		user = User.objects.get(username=request.session['logged_in'])
		sc = ServiceCall(customer=customer,end_user=enduser,site_name=sitename,site_address=siteaddress,contact_person_name1=contactpersonname1,
		contact_person_no1=contactpersonno1,contact_person_name2=contactpersonname2,
		contact_person_no2=contactpersonno2,req_date_of_installation_by_customer=reqdateinstall,name_of_product_supplied=nameofproduct
		,transformer_valve_size_details=transformervalvesize,customer_problem=cust_prob,
		sales_manager_request_no=salesmanagerrequestno,date=date,created_by=user)
		sc.save()
		request.session['servicecall'] = sc.id

	return render(request,'ticket/pages/product_model.html')

def email(request,ic_request):
	if request.method == 'POST':
		ic=ICRequest.objects.get(id=request.session['icrequestno'])
		heliumcylinder = request.POST['heliumcylinder']
		calgascylinder = request.POST['calgascylinder']
		sstubing = request.POST['sstubing']
		sstubingsize = request.POST['sstubingsize']
		standardlength_sstube = request.POST['standardlength_sstube']
		tubingaccessories = request.POST['tubingaccessories']
		flanges = request.POST['flanges']
		comm_mode = request.POST['comm_mode']
		ssupply = ScopeSupply(icrequest=ic,helium_cylinder=heliumcylinder,calibration_gas_cylinder=calgascylinder,ss_tubing=sstubing,ss_tubing_size=sstubingsize
		,standard_length_ss_tube=standardlength_sstube,tubing_accessories=tubingaccessories
		,flanges=flanges,communication_mode=comm_mode)
		ssupply.save()
	email = EmailMessage('New IC Request Created', '127.0.0.1:8000/ticket/pages/ic_info/'+ic_request, to=['vbanwari@qualitrolcorp.com'])
	email.send()
	return render(request,'ticket/pages/profile.html')

def email_pm(request,service_call):
	if request.method == 'POST':
		#print(service_call)
    		product_model = request.POST['product']	
    		quantity = request.POST['qty']
    		issue_reported = request.POST['issue_reported']
    		visit_required = request.POST['visit_required']
    		customer_req_date = request.POST['customer_req_date']
    		service = ServiceCall.objects.get(id=request.session['servicecall'])
    		product = ProductModel(service=service,
			product_model=product_model,quantity=quantity,
			issue_reported=issue_reported,
			visit_required=visit_required,
			customer_req_date=customer_req_date)
	product.save()
	email = EmailMessage('New Service Call Created', '127.0.0.1:8000/ticket/pages/sc_info/'+service_call, to=['vbanwari@qualitrolcorp.com'])
	email.send()
	return render(request,'ticket/pages/profile.html')

def reporting(request):
	return render(request,'ticket/pages/reporting.html')

def your_ic_request(request):
	user = User.objects.get(username=request.session['logged_in'])
	ic = ICRequest.objects.filter(created_by=user)
	return render(request,'ticket/pages/your_ic_request.html',{'output' : ic})
	
def your_service_call(request):
	user = User.objects.get(username=request.session['logged_in'])
	sc = ServiceCall.objects.filter(created_by=user)
	return render(request,'ticket/pages/your_service_call.html',{'output1' : sc})

def ic_info(request,ic1):
	print(ic1)
	ic = ICRequest.objects.get(id=ic1)
	return render(request,'ticket/pages/ic_info.html',{'output' : ic})
	
def sc_info(request,sc1):
	sc = ServiceCall.objects.get(id=sc1)
	return render(request,'ticket/pages/sc_info.html',{'output1' : sc})