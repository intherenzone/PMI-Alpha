#Create Django-Generated forms. Used for adding/editing objects in database. 
#Second section of forms.py used for generating searchable tables. 

#TODO CORRESPOND WITH USERS, CHANGE WHICH FIELDS ARE AVAILABLE TO BE SEARCHED BY
#ACCORDINGLY

from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton
from dal import autocomplete

class VendorForm(forms.ModelForm):
    class Meta:

        model = Vendor
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:

        model = Employee
        fields = '__all__'


class GoogleGroupForm(forms.ModelForm):
    class Meta:

        model = GoogleGroup
        fields = '__all__'


class PartnerForm(forms.ModelForm):
    class Meta:

        model = Partner
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = '__all__'

class ContractForm(forms.ModelForm):
    class Meta:

        model = Contract
        fields = '__all__'

class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department
        fields = '__all__'
    def __init__(self, *args, **kwargs):

        super(DepartmentForm, self).__init__(*args, **kwargs)
        # CHECK: TypedMultipleChoiceField
        self.fields['Employees']=forms.ModelChoiceField(queryset=Employee.objects.all())

class POCForm(forms.ModelForm):
    class Meta:

        model = POC
        fields = '__all__'


#KEY COMPONENT TO SEARCH TABLES. TO ADD/CHANGE SEARCH-BY-FIELDS EDIT THE ITEMS IN THE "FIELDSET"

class VendorListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
         Fieldset(
                    '<i class="fa fa-search"></i> Search Vendor Records',       
                    'LegalName',
                    'POC'
                ),
              Submit('submit', 'Apply Filter'),
    )

class EmployeeListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
         Fieldset(
                    '<i class="fa fa-search"></i> Search Employee Records',       
                    'FName',
                    'LName',
                    'HUBzone',
                    'VendorID',
                    'DateOfHire',
                    'EmployementStatus',
                    #'date_between',

                ),
                #'resource_first_name',
                #'resource_last_name',
                #'HUBzone',
                #'employment_status',
              Submit('submit', 'Apply Filter'),
    )


class GGListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
        Fieldset('<i class="fa fa-search"></i> Search Google Group Records'),

        HTML("""
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
            <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
            <div class="ui-widget">
                {{filter.form.as_p}}
                <button type="submit">Apply Filter</button>
            </div>
            <script type="text/javascript">
                $(function(){
                   $("#id_Name").autocomplete({
                        source: "getN/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                });
                    $("#id_Admin").autocomplete({
                        source: "getAD/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                function AutoCompleteSelectHandler(event, ui)
                {
                    var selectedObj = ui.item;
                }
            </script>
        """),
                    #'Name',
                    #'Admin'
                    #Submit('submit', 'Apply Filter'),
    )


class CustomerListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
         Fieldset(
                    '<i class="fa fa-search"></i> Search Customer Records',
                     'LegalName',
                     'Vendors',
                     'Employees',
                     'Partners',
                     'DBA',
                     'Address',
                     'City',
                     'ZipCode',
                     'State',
                     'Country',
                     'Phone',
                     'Fax',
                     'Email',
                     'DUNs',
                     'CAGE',
                     'POC',
                     'TIN',
                ),
              Submit('submit', 'Apply Filter'),
    )
    include_media = False

class ContractListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(

        Fieldset('<i class="fa fa-search"></i> Search Contract Records'),

        HTML("""
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
            <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
            <div class="ui-widget">
                {{filter.form.as_p}}
                <p> Notice: When you input Date, please follow the format "dd/mm/yyyy". </p>
                <button type="submit">Apply Filter</button>
            </div>

            <script type="text/javascript">

                $(function(){
                   $("#id_IssuingCompany").autocomplete({
                        source: "getIC/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_ContractNumber").autocomplete({
                        source: "getCN/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_DocumentLocation").autocomplete({
                        source: "getDL/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_OrganizationType").autocomplete({
                        source: "getOT/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_POC").autocomplete({
                        source: "getPOC/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_Status").autocomplete({
                        source: "getS/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                    $("#id_Comments").autocomplete({
                        source: "getC/",
                        select:function(event, ui){
                            AutoCompleteSelectHandler(event, ui)
                        },
                        minLength: 1,
                    });
                });

                function AutoCompleteSelectHandler(event, ui)
                {
                    var selectedObj = ui.item;
                }
            </script>
        """),
        # 'IssuingCompany',
        # 'ContractNumber',
        # 'DocumentLocation',
        # 'OrganizationType',
        # 'EffectiveDate',
        # 'EndDate',
        # 'StartDate',
        # 'Status',
        # 'Comments',
        #Submit('submit', 'Apply Filter'),
    )

class PartnerListFormHelper(FormHelper):
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
                    Fieldset('<i class="fa fa-search"></i> Search Contract Records'),
                    
                    HTML("""
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
                        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
                        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
                        <div class="ui-widget">
                            {{filter.form.as_p}}
                            <p> Notice: When you input Date, please follow the format "dd/mm/yyyy". </p>
                            <button type="submit">Apply Filter</button>
                        </div>
        
                        <script type="text/javascript">
        
                            $(function(){
                                $("#id_LegalName").autocomplete({
                                    source: "getLN/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Address").autocomplete({
                                    source: "getPA/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_CAGE").autocomplete({
                                    source: "getCAGE/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_City").autocomplete({
                                    source: "getPC/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_ZipCode").autocomplete({
                                    source: "getPZ/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_State").autocomplete({
                                    source: "getPS/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Country").autocomplete({
                                    source: "getPCOUNTRY/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Phone").autocomplete({
                                    source: "getPP/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Fax").autocomplete({
                                    source: "getPF/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Email").autocomplete({
                                    source: "getPE/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_DBA").autocomplete({
                                    source: "getDBA/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_DUNs").autocomplete({
                                    source: "getDUN/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_POC").autocomplete({
                                    source: "getPPOC/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_TIN").autocomplete({
                                    source: "getTIN/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                                $("#id_Type").autocomplete({
                                    source: "getTYPE/",
                                    select:function(event, ui){
                                        AutoCompleteSelectHandler(event, ui)
                                    },
                                    minLength: 1,
                                });
                            });
        
                            function AutoCompleteSelectHandler(event, ui)
                            {
                                var selectedObj = ui.item;
                            }
                        </script>
                    """),
    )


class DepartmentListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(
         Fieldset(
                    '<i class="fa fa-search"></i> Search Department Records',       
                    'ContractID',
                    'CustomerID',
                    'Name',
                    'Location',
                    'Fax',
                    'Supervisor',
                    'Phone',

                ),
              Submit('submit', 'Apply Filter'),
    )

class POCListFormHelper(FormHelper):    
    form_method = 'GET'
    FormHelper.form_class = 'form-horizontal'
    field_class = 'col-lg-6'
    label_class = 'col-lg-3'
    layout = Layout(

        Fieldset('<i class="fa fa-search"></i> Search POC Records'),

        HTML("""
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>
        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
        <div class="ui-widget">
            {{filter.form.as_p}}
            <button type="submit">Apply Filter</button>
        </div>
        <script type="text/javascript">
            $(function(){
               $("#id_FName").autocomplete({
                    source: "getFN/",
                    select:function(event, ui){
                        AutoCompleteSelectHandler(event, ui)
                    },
                    minLength: 1,
                });
               $("#id_LName").autocomplete({
                    source: "getLN/",
                    select:function(event, ui){
                        AutoCompleteSelectHandler(event, ui)
                    },
                    minLength: 1,
                });
               $("#id_Address").autocomplete({
                    source: "getA/",
                    select:function(event, ui){
                        AutoCompleteSelectHandler(event, ui)
                    },
                    minLength: 1,
                });
                $("#id_Phone").autocomplete({
                    source: "getP/",
                    select:function(event, ui){
                        AutoCompleteSelectHandler(event, ui)
                    },
                    minLength: 1,
                });
                $("#id_Email").autocomplete({
                    source: "getE/",
                    select:function(event, ui){
                        AutoCompleteSelectHandler(event, ui)
                    },
                    minLength: 1,
                });
            });
            function AutoCompleteSelectHandler(event, ui)
            {
                var selectedObj = ui.item;
            }
        </script>
    """),
                    #InlineField('FName'),
                    #InlineField('LName'),
                    #'PartnerID',
                    #'ContractID',
                    #'CustomerID',
                    #'Address',
                    #'Phone',
                    #'Email',


              #Submit('submit', 'Apply Filter'),
    )

