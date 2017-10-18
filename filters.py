#Used in conjunction with forms.py to create filterable tables. ie. search by field
#in each table. 

import django_filters
from .models import *
from django import forms
from dal import autocomplete

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
    LegalName = django_filters.ModelChoiceFilter(name='LegalName',queryset=Customer.objects.all(),
                                                 widget=autocomplete.ModelSelect2(url='LegalName-autocomplete'),
                                                 to_field_name='LegalName')

    Vendors = django_filters.ModelChoiceFilter(name='Vendors__LegalName', queryset=Customer.objects.all(),
                                               widget=autocomplete.ModelSelect2(url='Vendors-autocomplete'))
    Employees = django_filters.ModelChoiceFilter(name='Employees__LName', queryset=Customer.objects.all(),
                                                 widget=autocomplete.ModelSelect2(url='Employees-autocomplete'))
    Partners = django_filters.ModelChoiceFilter(name='Partners__LegalName', queryset=Customer.objects.all(),
                                                widget=autocomplete.ModelSelect2(url='Partners-autocomplete'))

    DBA = django_filters.Filter(name="DBA",
                                            widget=autocomplete.Select2(url='DBA-autocomplete'),)
    Address = django_filters.CharFilter(name="Address",
                                               widget=autocomplete.Select2(url='Address-autocomplete'))
    City = django_filters.CharFilter(name="City",
                                            widget=autocomplete.Select2(url='City-autocomplete'))
    ZipCode = django_filters.CharFilter(name="ZipCode",
                                               widget=autocomplete.Select2(url='ZipCode-autocomplete'))
    State = django_filters.CharFilter(name="State",
                                             widget=autocomplete.Select2(url='State-autocomplete'))
    Country = django_filters.CharFilter(name="Country",
                                               widget=autocomplete.Select2(url='Country-autocomplete'))
    Phone = django_filters.CharFilter(name="Phone",
                                             widget=autocomplete.Select2(url='Phone-autocomplete'))
    Fax = django_filters.CharFilter(name="Fax",
                                           widget=autocomplete.Select2(url='Fax-autocomplete'))
    Email = django_filters.CharFilter(name="Email",
                                             widget=autocomplete.Select2(url='Email-autocomplete'))
    DUNs = django_filters.CharFilter(name="DUNs",
                                            widget=autocomplete.Select2(url='DUNs-autocomplete'))
    CAGE = django_filters.CharFilter(name="CAGE",
                                            widget=autocomplete.Select2(url='CAGE-autocomplete'))
    POC = django_filters.CharFilter(name="POC",
                                           widget=autocomplete.Select2(url='POC-autocomplete'))
    TIN = django_filters.CharFilter(name="TIN",
                                           widget=autocomplete.Select2(url='TIN-autocomplete'))
    class Meta:
        model = Customer
        fields =  '__all__'
        order_by = ['pk']

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
        fields = ['LegalName', 'Address', 'City', 'ZipCode', 'State', 'Country', 'Phone','Fax', 'Email', 'DBA', 'DUNs','POC','TIN','Type']

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
