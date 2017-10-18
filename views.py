from django.shortcuts import render
from django_tables2 import RequestConfig
from .forms import *
from .models import *
from .tables import *
from .filters import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from watson import search as watson
from django.views.generic import ListView
from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
import json

# Autocomplete for Customer model
from dal import autocomplete
class LegalName_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName')
        if self.q:
            qs = qs.filter(LegalName__istartswith=self.q)
        return qs

class Vendors_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Vendor.objects.order_by('LegalName')
        if self.q:
            qs = qs.filter(LegalName__icontains=self.q)
        return qs

class Employees_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Employee.objects.order_by('LName').distinct()
        if self.q:
            qs = qs.filter(LName__icontains=self.q)
        return qs

class Partners_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Partner.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(LegalName__icontains=self.q)
        return qs

class DBA_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(DBA__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.DBA

    def get_result_value(self, item):
        return item.DBA

class Address_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(Address__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.Address

    def get_result_value(self, item):
        return item.Address

class City_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(City__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.City

    def get_result_value(self, item):
        return item.City

class ZipCode_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(ZipCode__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.ZipCode

    def get_result_value(self, item):
        return item.ZipCode

class State_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(State__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.State

    def get_result_value(self, item):
        return item.State

class Country_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(Country__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.Country

    def get_result_value(self, item):
        return item.Country

class Phone_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(Phone__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.Phone

    def get_result_value(self, item):
        return item.Phone

class Fax_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()

        if self.q:
            qs = qs.filter(Fax__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.Fax

    def get_result_value(self, item):
        return item.Fax

class Email_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()

        if self.q:
            qs = qs.filter(Email__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.Email

    def get_result_value(self, item):
        return item.Email

class DUNs_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()

        if self.q:
            qs = qs.filter(DUNs__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.DUNs

    def get_result_value(self, item):
        return item.DUNs

class CAGE_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(CAGE__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.CAGE

    def get_result_value(self, item):
        return item.CAGE

class POC_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(POC__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.POC

    def get_result_value(self, item):
        return item.POC

class TIN_autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.order_by('LegalName').distinct()
        if self.q:
            qs = qs.filter(TIN__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.TIN

    def get_result_value(self, item):
        return item.TIN

#Contract model
def getIC(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    IC = Contract.objects.order_by('IssuingCompany').filter(IssuingCompany__istartswith=q)
    results = []
    for ic in IC:
        IC_json = {}
        IC_json['value'] = ic.IssuingCompany
        if IC_json not in results:
            results.append(IC_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getCN(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    CN = Contract.objects.order_by('ContractNumber').filter(ContractNumber__istartswith=q)
    results = []
    for cn in CN:
        CN_json = {}
        CN_json['value'] = cn.ContractNumber
        if CN_json not in results:
            results.append(CN_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getDL(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    DL = Contract.objects.order_by('DocumentLocation').filter(DocumentLocation__istartswith=q)
    results = []
    for dl in DL:
        DL_json = {}
        DL_json['value'] = dl.DocumentLocation
        if DL_json not in results:
            results.append(DL_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getOT(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    OT = Contract.objects.order_by('OrganizationType').filter(OrganizationType__istartswith=q)
    results = []
    for ot in OT:
        OT_json = {}
        OT_json['value'] = ot.OrganizationType
        if OT_json not in results:
            results.append(OT_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getPOC(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    POC = Contract.objects.order_by('POC').filter(POC__istartswith=q)
    results = []
    for poc in POC:
        POC_json = {}
        POC_json['value'] = poc.POC
        if POC_json not in results:
            results.append(POC_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getS(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    S = Contract.objects.order_by('Status').filter(Status__istartswith=q)
    results = []
    for s in S:
        S_json = {}
        S_json['value'] = s.Status
        if S_json not in results:
            results.append(S_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getC(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    C = Contract.objects.order_by('Comments').filter(Comments__istartswith=q)
    results = []
    for c in C:
        C_json = {}
        C_json['value'] = c.Comments
        if C_json not in results:
            results.append(C_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

#POC model
def getFN(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    FN = POC.objects.order_by('FName').filter(FName__istartswith=q)
    results = []
    for fn in FN:
        FN_json = {}
        FN_json['value'] = fn.FName
        if FN_json not in results:
            results.append(FN_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getLN(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    LN = POC.objects.order_by('LName').filter(LName__istartswith=q)
    results = []
    for ln in LN:
        LN_json = {}
        LN_json['value'] = ln.LName
        if LN_json not in results:
            results.append(LN_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getA(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    A = POC.objects.order_by('Address').filter(Address__istartswith=q)
    results = []
    for a in A:
        A_json = {}
        A_json['value'] = a.Address
        if A_json not in results:
            results.append(A_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getP(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    P = POC.objects.order_by('Phone').filter(Phone__istartswith=q)
    results = []
    for p in P:
        P_json = {}
        P_json['value'] = p.Phone
        if P_json not in results:
            results.append(P_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getE(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    E = POC.objects.order_by('Email').filter(Email__istartswith=q)
    results = []
    for e in E:
        E_json = {}
        E_json['value'] = e.Email
        if E_json not in results:
            results.append(E_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

#GG model
def getN(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    N = GoogleGroup.objects.order_by('Name').filter(Name__istartswith=q)
    results = []
    for n in N:
        N_json = {}
        N_json['value'] = n.Name
        if N_json not in results:
            results.append(N_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def getAD(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    AD = GoogleGroup.objects.order_by('Admin').filter(Admin__istartswith=q)
    results = []
    for ad in AD:
        AD_json = {}
        AD_json['value'] = ad.Admin
        if AD_json not in results:
            results.append(AD_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


#Partner model
def getLN(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        LN = Partner.objects.order_by('LegalName').filter(LegalName_istartswith=q)
        results = []
        for ln in LN:
            LN_json = {}
            LN_json['value']=ln.LegalName
            if LN_json not in results:
                results.append(LN_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPA(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PA = Partner.objects.order_by('Address').filter(Address_istartswith=q)
        results = []
        for pa in PA:
            PA_json = {}
            PA_json['value']=pa.PA
            if PA_json not in results:
                results.append(PA_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getCAGE(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        CAGE = Partner.objects.order_by('CAGE').filter(CAGE_istartswith=q)
        results = []
        for cage in CAGE:
            CAGE_json = {}
            CAGE_json['value']=cage.CAGE
            if CAGE_json not in results:
                results.append(CAGE_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPC(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PC = Partner.objects.order_by('City').filter(City_istartswith=q)
        results = []
        for pc in PC:
            PC_json = {}
            PC_json['value']=pc.City
            if PC_json not in results:
                results.append(PC_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPZ(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PZ = Partner.objects.order_by('ZipCode').filter(ZipCode_istartswith=q)
        results = []
        for pz in PZ:
            PZ_json = {}
            PZ_json['value']=pz.ZipCode
            if PZ_json not in results:
                results.append(PZ_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPS(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PS = Partner.objects.order_by('State').filter(State_istartswith=q)
        results = []
        for ps in PS:
            PS_json = {}
            PS_json['value']=ps.State
            if PS_json not in results:
                results.append(PS_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPCOUNTRY(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PCOUNTRY = Partner.objects.order_by('Country').filter(Country_istartswith=q)
        results = []
        for pcountry in PCOUNTRY:
            PCOUNTRY_json = {}
            PCOUNTRY_json['value']=pcountry.Country
            if PCOUNTRY_json not in results:
                results.append(PCOUNTRY_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPP(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PP = Partner.objects.order_by('Phone').filter(Phone_istartswith=q)
        results = []
        for pp in PP:
            PP_json = {}
            PP_json['value']=pp.Phone
            if PP_json not in results:
                results.append(PP_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPF(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PF = Partner.objects.order_by('Fax').filter(Fax_istartswith=q)
        results = []
        for pf in PF:
            PF_json = {}
            PF_json['value']=pf.Fax
            if PF_json not in results:
                results.append(PF_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPE(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PE = Partner.objects.order_by('Email').filter(Email_istartswith=q)
        results = []
        for pe in PE:
            PE_json = {}
            PE_json['value']=pe.Email
            if PE_json not in results:
                results.append(PE_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getDBA(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        DBA = Partner.objects.order_by('DBA').filter(DBA_istartswith=q)
        results = []
        for dba in DBA:
            DBA_json = {}
            DBA_json['value']=dba.DBA
            if DBA_json not in results:
                results.append(DBA_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getDUN(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        DUN = Partner.objects.order_by('DUNs').filter(DUNs_istartswith=q)
        results = []
        for dun in DUN:
            DUN_json = {}
            DUN_json['value']=dun.DUNs
            if DUN_json not in results:
                results.append(DUN_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getPPOC(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        PPOC = Partner.objects.order_by('POC').filter(POC_istartswith=q)
        results = []
        for ppoc in PPOC:
            PPOC_json = {}
            PPOC_json['value']=ppoc.POC
            if PPOC_json not in results:
                results.append(PPOC_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getTIN(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        TIN = Partner.objects.order_by('TIN').filter(TIN_istartswith=q)
        results = []
        for tin in TIN:
            TIN_json = {}
            TIN_json['value']=tin.TIN
            if TIN_json not in results:
                results.append(TIN_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def getTYPE(request):
    if request.is_ajax():
        q = request.GET.get('tern','')
        TYPE = Partner.objects.order_by('Type').filter(Type_istartswith=q)
        results = []
        for type in TYPE:
            TYPE_json = {}
            TYPE_json['value']=type.Type
            if TYPE_json not in results:
                results.append(TYPE_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

#Detail Views -> Shows detailed Object Info from table.
class Vendor_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Vendor'
    model = Vendor
    template_name = 'database/detail.html'

class Employee_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Employee'
    model = Employee
    template_name = 'database/detail.html'

class GoogleGroup_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.GoogleGroup'
    model = GoogleGroup
    template_name = 'database/detail.html'

class Customer_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Customer'
    model = Customer
    template_name = 'database/detail.html'

class Contract_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Contract'
    model = Contract
    template_name = 'database/detail.html'

class Partner_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Partner'
    model = Partner
    template_name = 'database/detail.html'

class Department_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.Department'
    model = Department
    template_name = 'database/detail.html'

class POC_DetailView(PermissionRequiredMixin,generic.DetailView):
    permission_required = 'database.POC'
    model = POC
    template_name = 'database/detail.html'

#Shows All Tables in One Page
@login_required
def tables(request):
    vendor_table = VendorTable(Vendor.objects.all())
    employee_table = EmployeeTable(Employee.objects.all())
    googlegroup_table = GoogleGroupTable(GoogleGroup.objects.all())
    customer_table = CustomerTable(Customer.objects.all())
    contract_table = ContractTable(Contract.objects.all())
    partner_table = PartnerTable(Partner.objects.all())
    department_table = DepartmentTable(Department.objects.all())
    department_employee_table = Department_EmployeeTable(Department_Employee.objects.all())
    contract_employee_table = Contract_EmployeeTable(Contract_Employee.objects.all())
    customer_vendor_table = Customer_VendorTable(Customer_Vendor.objects.all())
    customer_employee_table = Customer_EmployeeTable(Customer_Employee.objects.all())
    customer_partner_table = Customer_PartnerTable(Customer_Partner.objects.all())
    poc_table = POCTable(POC.objects.all())
    vendor_contract_table = Vendor_ContractTable(Vendor_Contract.objects.all())
    googlegroup_employee_table = GoogleGroup_EmployeeTable(GoogleGroup_Employee.objects.all())


    RequestConfig(request).configure(vendor_table)
    RequestConfig(request).configure(employee_table)
    RequestConfig(request).configure(googlegroup_table)
    RequestConfig(request).configure(customer_table)
    RequestConfig(request).configure(contract_table)
    RequestConfig(request).configure(partner_table)
    RequestConfig(request).configure(department_table)
    RequestConfig(request).configure(department_employee_table)
    RequestConfig(request).configure(contract_employee_table)
    RequestConfig(request).configure(customer_vendor_table)
    RequestConfig(request).configure(customer_employee_table)
    RequestConfig(request).configure(customer_partner_table)
    RequestConfig(request).configure(poc_table)
    RequestConfig(request).configure(vendor_contract_table)
    RequestConfig(request).configure(googlegroup_employee_table)

    # search_results = watson.search("Noah",  exclude=(Employee,))

    # for result in search_results:
    #     print (result.title, result.url)

    return render(request, 'database/tables.html',
    	{'vendor': vendor_table,
    	'employee':employee_table,
    	'googlegroup':googlegroup_table,
    	'customer': customer_table,
    	'contract':contract_table,
    	'partner':partner_table,
    	'department': department_table,
    	'department_employee':department_employee_table,
    	'contract_employee':contract_employee_table,
    	'customer_vendor': customer_vendor_table,
    	'customer_employee':customer_employee_table,
    	'customer_partner':customer_partner_table,
    	'poc': poc_table,
    	'vendor_contract':vendor_contract_table,
    	'googlegroup_employee':googlegroup_employee_table,
        })


#add_* --> renders add page to add new objects to database
@login_required
def add_vendor(request):
    form = VendorForm(request.POST or None);
    name = "Vendor";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)

@login_required
def add_employee(request):
    form = EmployeeForm(request.POST or None);
    name = "Employee";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')

    return render(request, 'database/add_new.html', context)

@login_required
def add_gg(request):
    form = GoogleGroupForm(request.POST or None);
    name = "Google Group";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)

@login_required
def add_customer(request):
    permission_required = 'database.Customer'
    form = CustomerForm(request.POST or None);
    name = "Customer";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)

@login_required
def add_contract(request):
    form = ContractForm(request.POST or None);
    name = "Contract";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)

@login_required
def add_partner(request):
    form = PartnerForm(request.POST or None);
    name = "Partner";
    context = {
        'form' : form,
        'name' : name

    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)


@login_required
def add_department(request):
    form = DepartmentForm(request.POST or None);
    name = "Department";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/dashboard/')


    return render(request, 'database/add_new.html', context)

@login_required
def add_poc(request):
    form = POCForm(request.POST or None);
    name = "POC"
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/database/')


    return render(request, 'database/add_new.html', context)


#HTML PAGES USED FOR REDIRECTION
@login_required
def search (request):
    return render(request, 'database/search.html')
@login_required
def dashboard(request):
    return render(request, 'database/dashboard.html', {})
@login_required
def add_record(request):
    return render(request, 'database/add_record.html', {})
@login_required
def basic_search(request):
    return render(request, 'database/basic_search.html', {})
# Scrap for now: select_table is now advanced search
@login_required
def advanced_search(request):
    return render(request, 'database/advanced_search.html', {})
@login_required
def select_table(request): # this is now advanced search
    return render(request, 'database/select_view.html', {})

#ADVANCED TABLES, SEARCH/FILTER
class VendorListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Vendor'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Vendor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VendorListView, self).get_context_data(**kwargs)
        filter = VendorListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = VendorListFormHelper()
        table = VendorTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class EmployeeListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Employee'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        filter = EmployeeListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = EmployeeListFormHelper()
        table = EmployeeTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class GGListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.GoogleGroup'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return GoogleGroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GGListView, self).get_context_data(**kwargs)
        filter = GGListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = GGListFormHelper()
        table = GoogleGroupTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class CustomerListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Customer'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        filter = CustomerListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = CustomerListFormHelper()
        table = CustomerTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context
        
class ContractListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Contract'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Contract.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ContractListView, self).get_context_data(**kwargs)
        filter = ContractListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = ContractListFormHelper()
        table = ContractTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class PartnerListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Partner'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Partner.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PartnerListView, self).get_context_data(**kwargs)
        filter = PartnerListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = PartnerListFormHelper()
        table = PartnerTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class DepartmentListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.Department'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return Department.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        filter = DepartmentListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = DepartmentListFormHelper()
        table = DepartmentTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

class POCListView(PermissionRequiredMixin,TemplateView):
    permission_required = 'database.POC'
    template_name = 'database/searchable.html'

    def get_queryset(self, **kwargs):
        return POC.objects.all()

    def get_context_data(self, **kwargs):
        context = super(POCListView, self).get_context_data(**kwargs)
        filter = POCListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = POCListFormHelper()
        table = POCTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

#class DepartmentAutocomplete(autocomplete.Select2QuerySetView):
    # autocomplete function for ProfessionalDevelopment class
 ##
   #     qs = Department.objects.all()
#
 #       if self.q:
  ##
    #    return qs
