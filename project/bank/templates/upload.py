from django import forms
class CustomerDocx(forms.Form):
    username = forms.CharField(label="Enter user name", max_length = 30)
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length = 10)
    Aadhar = forms.FileField() # for creating file input
    PAN = forms.FileField() # for creating file input
