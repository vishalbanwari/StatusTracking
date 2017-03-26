from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class ICRequest(models.Model):
    customer = models.CharField(max_length=200)
    end_user = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)
    contact_person_name1 = models.CharField(max_length=255)
    contact_person_no1 = models.IntegerField(10)
    contact_person_name2 = models.CharField(max_length=255,default=0)
    contact_person_no2 = models.IntegerField(10,default=0)
    req_date_of_installation_by_customer = models.DateField('Req Date Installation of Customer')
    pre_sign_off_sheet_status = models.CharField(max_length=255)
    site_status = models.CharField(max_length=255)
    name_of_product_supplied = models.CharField(max_length=255)
    quantity = models.IntegerField(5)
    transformer_valve_size_details = models.CharField(max_length=255)
    material_reached_at_site = models.CharField(max_length=255)
    sales_manager_request_no = models.CharField(max_length=255)
    date = models.DateField('Today')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str(self.id)

class ScopeSupply(models.Model):
    icrequest = models.ForeignKey(ICRequest, on_delete=models.CASCADE)
    helium_cylinder = models.CharField(max_length=255)
    calibration_gas_cylinder = models.CharField(max_length=255)
    ss_tubing = models.CharField(max_length=255)
    ss_tubing_size = models.CharField(max_length=255)
    standard_length_ss_tube = models.CharField(max_length=255)
    tubing_accessories = models.CharField(max_length=255)
    flanges = models.CharField(max_length=255)
    communication_mode = models.CharField(max_length=255)
    def __str__(self):
        return str(self.icrequest)

class ServiceCall(models.Model):
    customer = models.CharField(max_length=200)
    end_user = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)
    contact_person_name1 = models.CharField(max_length=255)
    contact_person_no1 = models.IntegerField(10)
    contact_person_name2 = models.CharField(max_length=255,default=0)
    contact_person_no2 = models.IntegerField(10,default=0)
    req_date_of_installation_by_customer = models.DateField('Req Date Installation of Customer')
    name_of_product_supplied = models.CharField(max_length=255)
    transformer_valve_size_details = models.CharField(max_length=255)
    customer_problem = models.CharField(max_length=255)
    sales_manager_request_no = models.CharField(max_length=255)
    date = models.DateField('Today')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str(self.id)

class ProductModel(models.Model):
    service = models.ForeignKey(ServiceCall, on_delete=models.CASCADE)
    product_model = models.CharField(max_length=255)
    quantity = models.IntegerField(max_length=255)
    issue_reported = models.CharField(max_length=255)
    visit_required = models.CharField(max_length=255)
    customer_req_date = models.DateField('Customer Req Date')
    def __str__(self):
        return str(self.service)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.customer_name)

class EndUser(models.Model):
    end_user_name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.end_user_name)





    
    
    
    
    



    
    




