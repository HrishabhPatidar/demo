from .models import Contact
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class ContactForms(forms.ModelForm):
    first_name = forms.CharField( required=True,
                                  widget=forms.TextInput(
                                      attrs={
                                          'placeholder':'First Name'
                                      }
                                  ))
    last_name = forms.CharField(     required=True,
                                     widget=forms.TextInput(
                                         attrs={
                                             'placeholder':'Last Name'
                                         }
                                     ))
    contact_email = forms.EmailField(     required=True,
                                          widget=forms.EmailInput(
                                              attrs={
                                                  'placeholder':'abc@example.com'
                                              }
                                          ))
    contact_no = forms.IntegerField(     required=True,
                                         widget=forms.NumberInput(
                                             attrs={
                                                 'placeholder':'Phone '
                                             }
                                         ))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'placeholder':'Message'
                                  }
                              )               )

    helper = FormHelper()
    helper.form_show_labels=False
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.field_class = 'col-sm-8 col-md-6 col-sm-offset-2 col-md-offset-3'
    helper.layout = Layout(
        Field('first_name', style='width:80%;padding:5px;margin:7px;border-radius:5px;'),
        Field('last_name',style='width:80%;padding:5px;margin:7px;border-radius:5px;'),
        Field('contact_email', style='width:80%;padding:5px;margin:7px;border-radius:5px;'),
        Field('contact_no', style='width:80%;padding:5px;margin:7px;border-radius:5px;'),
        Field('message', rows=7 ,style='width:80%;padding:5px;margin:7px;border-radius:5px;'),

    )

    class Meta:
        model = Contact
        fields = [
            'first_name','last_name','contact_email', 'contact_no','message',
        ]

