from django.conf.urls import url
from . import views
from django.conf.urls import include
from .models import *
from django.contrib import admin

urlpatterns = [
   url(r'^$', views.tables, name='tables'),
   url(r'^home/$', views.dashboard, name= 'home'),

   url(r'^vendor/(?P<pk>[0-9]+)/$', views.Vendor_DetailView.as_view(), name='vendor_detail'),
   url(r'^employee/(?P<pk>[0-9]+)/$', views.Employee_DetailView.as_view(), name='employee_detail'),
   url(r'^googlegroup/(?P<pk>[0-9]+)/$', views.GoogleGroup_DetailView.as_view(), name='googlegroup_detail'),
   url(r'^customer/(?P<pk>[0-9]+)/$', views.Customer_DetailView.as_view(), name='customer_detail'),
   url(r'^contract/(?P<pk>[0-9]+)/$', views.Contract_DetailView.as_view(), name='contract_detail'),
   url(r'^partner/(?P<pk>[0-9]+)/$', views.Partner_DetailView.as_view(), name='partner_detail'),
   url(r'^department/(?P<pk>[0-9]+)/$', views.Department_DetailView.as_view(), name='department_detail'),
   url(r'^poc/(?P<pk>[0-9]+)/$', views.POC_DetailView.as_view(), name='poc_detail'),

   #RENDERS ADD OBJECT PAGES USING MODELFORMS
   url(r'^add_vendor/$', views.add_vendor, name= 'add vendor'),
   url(r'^add_employee/$', views.add_employee, name= 'add employee'),
   url(r'^add_gg/$', views.add_gg, name= 'add googlegroup'),
   url(r'^add_customer/$', views.add_customer, name= 'add customer'),
   url(r'^add_contract/$', views.add_contract, name= 'add contract'),
   url(r'^add_partner/$', views.add_partner, name= 'add partner'),
   url(r'^add_department/$', views.add_department, name= 'add department'),
   url(r'^add_poc/$', views.add_poc, name= 'add poc'),


   #BASIC SEARCH
   url(r'^search/', include("watson.urls", namespace="watson"), {'template_name' : 'database/search_results.html',}),


   #USD WITH SIDE BAR TO REDIRECT
   url(r'^dashboard/$', views.dashboard, name= 'dashboard'),
   url(r'^add_record/$', views.add_record, name= 'add record'),
   url(r'^basic_search/$', views.basic_search, name= 'basic search'),
   url(r'^advanced_search/$', views.advanced_search, name= 'advanced search'),
   url(r'^select/$', views.select_table, name= 'select table'),
   url(r'^admin/$', admin.site.urls ),



   #SELECT TABLE, DISPLAYS SEARCHABLE TABLE
    url(r'^vendors/$', views.VendorListView.as_view(), name="vendor table"),
    url(r'^employees/$', views.EmployeeListView.as_view(), name="employee table"),
    url(r'^GoogleGroups/$', views.GGListView.as_view(), name="google table"),
    url(r'^Customers/$', views.CustomerListView.as_view(), name="customer table"),
    url(r'^Contracts/$', views.ContractListView.as_view(), name="contract table"),
    url(r'^Partners/$', views.PartnerListView.as_view(), name="partner table"),
    url(r'^departments/$', views.DepartmentListView.as_view(), name="department table"),
    url(r'^POCs/$', views.POCListView.as_view(), name="poc table"),

    #Autocomplete for Customers
    url(r'^Customers/LegalName-autocomplete/$', views.LegalName_autocomplete.as_view(),
        name='LegalName-autocomplete', ),
    url(r'^Customers/Vendors-autocomplete/$', views.Vendors_autocomplete.as_view(),
        name='Vendors-autocomplete', ),
    url(r'^Customers/Employees-autocomplete/$', views.Employees_autocomplete.as_view(),
        name='Employees-autocomplete', ),
    url(r'^Customers/Partners-autocomplete/$', views.Partners_autocomplete.as_view(),
        name='Partners-autocomplete', ),
    url(r'^Customers/DBA-autocomplete/$', views.DBA_autocomplete.as_view(),
        name='DBA-autocomplete', ),
    url(r'^Customers/Address-autocomplete/$', views.Address_autocomplete.as_view(),
        name='Address-autocomplete', ),
    url(r'^Customers/City-autocomplete/$', views.City_autocomplete.as_view(),
        name='City-autocomplete', ),
    url(r'^Customers/ZipCode-autocomplete/$', views.ZipCode_autocomplete.as_view(),
        name='ZipCode-autocomplete', ),
    url(r'^Customers/State-autocomplete/$', views.State_autocomplete.as_view(),
        name='State-autocomplete', ),
    url(r'^Customers/Country-autocomplete/$', views.Country_autocomplete.as_view(),
        name='Country-autocomplete', ),
    url(r'^Customers/Phone-autocomplete/$', views.Phone_autocomplete.as_view(),
        name='Phone-autocomplete', ),
    url(r'^Customers/Fax-autocomplete/$', views.Fax_autocomplete.as_view(),
        name='Fax-autocomplete', ),
    url(r'^Customers/Email-autocomplete/$', views.Email_autocomplete.as_view(),
        name='Email-autocomplete', ),
    url(r'^Customers/DUNs-autocomplete/$', views.DUNs_autocomplete.as_view(),
        name='DUNs-autocomplete', ),
    url(r'^Customers/CAGE-autocomplete/$', views.CAGE_autocomplete.as_view(),
        name='CAGE-autocomplete', ),
    url(r'^Customers/POC-autocomplete/$', views.POC_autocomplete.as_view(),
        name='POC-autocomplete', ),
    url(r'^Customers/TIN-autocomplete/$', views.TIN_autocomplete.as_view(),
        name='TIN-autocomplete', ),
    #AutoComplete for Contract
    url(r'^Contracts/getIC/$', views.getIC, name='get_IC'),
    url(r'^Contracts/getCN/$', views.getCN, name='get_CN'),
    url(r'^Contracts/getDL/$', views.getDL, name='get_DL'),
    url(r'^Contracts/getOT/$', views.getOT, name='get_OT'),
    url(r'^Contracts/getPOC/$', views.getPOC, name='get_POC'),
    url(r'^Contracts/getS/$', views.getS, name='get_S'),
    url(r'^Contracts/getC/$', views.getC, name='get_C'),

    #AutoComplete for POC
    url(r'^POCs/getFN/$', views.getFN, name='get_FN'),
    url(r'^POCs/getLN/$', views.getLN, name='get_LN'),
    url(r'^POCs/getA/$', views.getA, name='get_A'),
    url(r'^POCs/getP/$', views.getP, name='get_P'),
    url(r'^POCs/getE/$', views.getE, name='get_E'),

    # AutoComplete for GG
    url(r'^GoogleGroups/getN/$', views.getN, name='get_N'),
    url(r'^GoogleGroups/getAD/$', views.getAD, name='get_AD'),
               
    #AutoComplete for Partner
    url(r'^Partner/getLN/$', views.getLN, name='get_LN'),
    url(r'^Partner/getPA/$', views.getPA, name='get_PA'),
    url(r'^Partner/getCAGE/$', views.getCAGE, name='get_CAGE'),
    url(r'^Partner/getPC/$', views.getPC, name='get_PC'),
    url(r'^Partner/getPZ/$', views.getPZ, name='get_PZ'),
    url(r'^Partner/getPS/$', views.getPS, name='get_PS'),
    url(r'^Partner/getPCOUNTRY/$', views.getPCOUNTRY, name='get_PCOUNTRY'),
    url(r'^Partner/getPP/$', views.getPP, name='get_PP'),
    url(r'^Partner/getPF/$', views.getPF, name='get_PF'),
    url(r'^Partner/getPE/$', views.getPE, name='get_PE'),
    url(r'^Partner/getDBA/$', views.getDBA, name='get_DBA'),
    url(r'^Partner/getDUN/$', views.getDUN, name='get_DUN'),
    url(r'^Partner/getPPOC/$', views.getPPOC, name='get_PPOC'),
    url(r'^Partner/getTIN/$', views.getTIN, name='get_TIN'),
    url(r'^Partner/getTYPE/$', views.getTYPE, name='get_TYPE'),



]
