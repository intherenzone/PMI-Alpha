#Used in conjunction with forms.py to create filterable tables. ie. search by field
#in each table. 

import django_filters
from .models import *
from django import forms


class VendorListFilter(django_filters.FilterSet):

  class Meta:
    model = Vendor
    fields =  '__all__'
    order_by = ['pk']

class EmployeeListFilter(django_filters.FilterSet):

  class Meta:
    model = Employee
    fields =  '__all__'
    #testing this
    date_between = django_filters.DateFromToRangeFilter(name='DateOfHire',
                                                             label='Date of Hire (Between)')
    order_by = ['pk']

class GGListFilter(django_filters.FilterSet):
  Name = django_filters.CharFilter(lookup_expr='iexact')
  Admin = django_filters.CharFilter(lookup_expr='iexact')
  class Meta:
    model = GoogleGroup
    fields = ['Name','Admin']
    #fields =  '__all__'
    #order_by = ['pk']

class CustomerListFilter(django_filters.FilterSet):
 LegalName = django_filters.CharFilter(lookup_expr='iexact')
 DBA = django_filters.CharFilter(lookup_expr='iexact')
 Address = django_filters.CharFilter(lookup_expr='iexact')
 City = django_filters.CharFilter(lookup_expr='iexact')
 ZipCode = django_filters.CharFilter(lookup_expr='iexact')
 State = django_filters.CharFilter(lookup_expr='iexact')
 Country = django_filters.CharFilter(lookup_expr='iexact')
 Phone = django_filters.CharFilter(lookup_expr='iexact')
 Fax = django_filters.CharFilter(lookup_expr='iexact')
 Email = django_filters.CharFilter(lookup_expr='iexact')
 DUNs = django_filters.CharFilter(lookup_expr='iexact')
 CAGE = django_filters.CharFilter(lookup_expr='iexact')
 POC = django_filters.CharFilter(lookup_expr='iexact')
 TIN = django_filters.CharFilter(lookup_expr='iexact')
 class Meta:
    model = Customer
    fields = ['LegalName','DBA','Address','City','ZipCode','State','Country','Phone','Fax','Email','DUNs','CAGE','POC','TIN']
    #fields =  '__all__'
    #order_by = ['pk']

class ContractListFilter(django_filters.FilterSet):
  IssuingCompany = django_filters.CharFilter(lookup_expr='iexact')
  ContractNumber = django_filters.CharFilter(lookup_expr='iexact')
  DocumentLocation = django_filters.CharFilter(lookup_expr='iexact')
  OrganizationType = django_filters.CharFilter(lookup_expr='iexact')
  POC = django_filters.CharFilter(lookup_expr='iexact')
  Status = django_filters.CharFilter(lookup_expr='iexact')
  Comments = django_filters.CharFilter(lookup_expr='iexact')
  EffectiveDate = django_filters.DateFilter(lookup_expr='exact')
  EndDate = django_filters.DateFilter(lookup_expr='exact')
  StartDate = django_filters.DateFilter(lookup_expr='exact')
  class Meta:
    model = Contract
    fields = ['CustomerID','IssuingCompany','ContractNumber','DocumentLocation','OrganizationType','POC','Status',
              'Comments','EffectiveDate','EndDate','StartDate']
    #fields = '__all__'
    #order_by = ['pk']

class PartnerListFilter(django_filters.FilterSet):
    LegalName = django_filters.CharFilter(lookup_expr='iexact')
    Address = django_filters.CharFilter(lookup_expr='iexact')
    CAGE = django_filters.CharFilter(lookup_expr='iexact')
    City = django_filters.CharFilter(lookup_expr='iexact')
    ZipCode = django_filters.CharFilter(lookup_expr='iexact')
    State = django_filters.CharFilter(lookup_expr='iexact')
    Country = django_filters.CharFilter(lookup_expr='iexact')
    Phone = django_filters.CharFilter(lookup_expr='iexact')
    Fax = django_filters.CharFilter(lookup_expr='iexact')
    Email = django_filters.CharFilter(lookup_expr='iexact')
    DBA = django_filters.CharFilter(lookup_expr='iexact')
    DUNs = django_filters.CharFilter(lookup_expr='iexact')
    POC = django_filters.CharFilter(lookup_expr='iexact')
    TIN = django_filters.CharFilter(lookup_expr='iexact')
    Type = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Partner
        fields = ['LegalName', 'Address', 'CAGE', 'City', 'ZipCode', 'State', 'Country', 'Phone', 'Fax', 'Email', 'DBA', 'DUNs', 'POC', 'TIN', 'Type']

class DepartmentListFilter(django_filters.FilterSet):

  class Meta:
    model = Department
    fields =  '__all__'
    order_by = ['pk']

class POCListFilter(django_filters.FilterSet):
  FName = django_filters.CharFilter(lookup_expr='iexact')
  LName = django_filters.CharFilter(lookup_expr='iexact')
  Address = django_filters.CharFilter(lookup_expr='iexact')
  Phone = django_filters.CharFilter(lookup_expr='iexact')
  Email = django_filters.CharFilter(lookup_expr='iexact')
  class Meta:
    model = POC
    fields = ['PartnerID','ContractID','CustomerID','FName','LName','Address','Phone','Email']
    #fields =  '__all__'
    #order_by = ['pk']
