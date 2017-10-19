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
    url(r'^Partners/getLN/$', views.getLN, name='get_LN'),
    url(r'^Partners/getPA/$', views.getPA, name='get_PA'),
    url(r'^Partners/getCAG/$', views.getCAG, name='get_CAG'),
    url(r'^Partners/getPC/$', views.getPC, name='get_PC'),
    url(r'^Partners/getPZ/$', views.getPZ, name='get_PZ'),
    url(r'^Partners/getPS/$', views.getPS, name='get_PS'),
    url(r'^Partners/getPCOUNTRY/$', views.getPCOUNTRY, name='get_PCOUNTRY'),
    url(r'^Partners/getPP/$', views.getPP, name='get_PP'),
    url(r'^Partners/getPF/$', views.getPF, name='get_PF'),
    url(r'^Partners/getPE/$', views.getPE, name='get_PE'),
    url(r'^Partners/getDBA/$', views.getDBA, name='get_DBA'),
    url(r'^Partners/getDUN/$', views.getDUN, name='get_DUN'),
    url(r'^Partners/getPPOC/$', views.getPPOC, name='get_PPOC'),
    url(r'^Partners/getTIN/$', views.getTIN, name='get_TIN'),
    url(r'^Partners/getTYPE/$', views.getTYPE, name='get_TYPE'),

    #AutoComplete for customer
    url(r'^Customers/getCLN/$', views.getCLN, name='get_CLN'),
    url(r'^Customers/getCDBA/$', views.getCDBA, name='get_CDBA'),
    url(r'^Customers/getCA/$', views.getCA, name='get_CA'),
    url(r'^Customers/getCC/$', views.getCC, name='get_CC'),
    url(r'^Customers/getCZ/$', views.getCZ, name='get_CZ'),
    url(r'^Customers/getCS/$', views.getCS, name='get_CS'),
    url(r'^Customers/getCCOUNTRY/$', views.getCCOUNTRY, name='get_CCOUNTRY'),
    url(r'^Customers/getCP/$', views.getCP, name='get_CP'),
    url(r'^Customers/getCF/$', views.getCF, name='get_CF'),
    url(r'^Customers/getCE/$', views.getCE, name='get_CE'),
    url(r'^Customers/getCDUN/$', views.getCDUN, name='get_CDUN'),
    url(r'^Customers/getCCAGE/$', views.getCCAGE, name='get_CCAGE'),
    url(r'^Customers/getCPOC/$', views.getCPOC, name='get_CPOC'),
    url(r'^Customers/getCTIN/$', views.getCTIN, name='get_CTIN'),

    #Edit Customer
    url(r'^customer/(?P<pk>[0-9]+)/edit$', views.CustomerUpdate.as_view(), name='edit customer'),



]
