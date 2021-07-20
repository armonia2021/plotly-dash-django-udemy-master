from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome*','class':"form-control",'id':'name'}))#,'data-sb-validations':"required"
    your_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email*','class':"form-control",'id':'email'}))#,'data-sb-validations':"required,email"
    your_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefono*','class':"form-control",'id':'phone'}))#,'data-sb-validations':"required"
    your_message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Inserire qui il messaggio*','class':"form-control",'id':'message','rows':8}))#,'data-sb-validations':"required"
    #my_cc = forms.BooleanField(required=False)


import pymongo
from pymongo import MongoClient
import ssl
import datetime
import pandas as pd
# Sistemare tutto
client = pymongo.MongoClient("mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
                #db = client.test
db = client['ArmoniaBot']
col = db['DatabaseDietabit']
lista = col.find()
FOOD_CHOICES = []
food = []
for lis in lista:
    food.append((lis['Nome']))
col = db['DatabaseCibo']
lista = col.find()

for lis in lista:
    food.append((lis['Nome']))
col = db['DatabaseBDA']
lista = col.find()

for lis in lista:
    food.append((lis['Nome']))
col = db['SushiDB']
lista = col.find()

for lis in lista:
    food.append((lis['Name']))
food.sort()
for fod in food:
    FOOD_CHOICES.append((fod, fod))
pasti = [('Colazione','Colazione'),('Pranzo','Pranzo'),('Cena','Cena'),('Merenda','Merenda')]

class SearchFood(forms.Form):
    #search_name= forms.CharField(label='Che alimento vuoi inserire?', widget=forms.Select(choices=FOOD_CHOICES))
    search_name = forms.ChoiceField(help_text = "Enter your Name",choices=FOOD_CHOICES,widget=forms.Select(attrs={'class':"form-control form-control-user",'text-align':'center'}))
    #search_name = forms.CharField(choices=FOOD_CHOICES, widget=forms.TextInput(attrs={'placeholder': 'Inserisci alimento'}))
    # pasto = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.RadioSelect,
    #     choices=pasti,
    # )
    pasto = forms.ChoiceField(choices=pasti,widget=forms.Select(attrs={'class':"form-control form-control-user"}))
    data = forms.DateField(initial=datetime.date.today,widget=forms.SelectDateWidget(attrs={'placeholder': '__/__/____', 'class':"form-control form-control-user",'auto_now_add':'True'}))#,'auto_now':'True'
    qty = forms.DecimalField(widget=forms.NumberInput(attrs={'class':"form-control form-control-user"}))

# from .fields import ListTextWidget
# pasti = [('Colazione','Colazione'),('Pranzo','Pranzo'),('Cena','Cena'),('Merenda','Merenda')]
# class FormForm(forms.Form):
#    char_field_with_list = forms.CharField(required=True)
#    pasto = forms.MultipleChoiceField(
#        required=False,
#        widget=forms.RadioSelect,
#        choices=pasti,
#    )
#    data = forms.DateField(widget=forms.SelectDateWidget(attrs={'placeholder': '__/__/____', 'class': 'date',}))
#
#    def __init__(self, *args, **kwargs):
#       _country_list = kwargs.pop('data_list', None)
#       super(FormForm, self).__init__(*args, **kwargs)
#
#     # the "name" parameter will allow you to use the same widget more than once in the same
#     # form, not setting this parameter differently will cuse all inputs display the
#     # same list.
#       self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_country_list, name='country-list')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':"form-control form-control-user", 'id':"exampleFirstName"}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':"form-control form-control-user", 'id':"exampleLastName"}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class':"form-control form-control-user", 'id':"exampleUserName"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Indirizzo email', 'class': "form-control form-control-user", 'id': "exampleInputEmail"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': "form-control form-control-user", 'id': "exampleInputPassword"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password', 'class': "form-control form-control-user",
               'id': "exampleRepeatPassword"}))
    class Meta:
        model = User
        fields = ("first_name", "last_name","username","email","password1","password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.is_staff = True
            user.save()
        return user

# class NewUserForm(UserCreationForm):
# 	username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class':"form-control form-control-user", 'id':"exampleFirstName"}))
# 	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Indirizzo email','class':"form-control form-control-user", 'id':"exampleInputEmail"}))
# 	password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':"form-control form-control-user", 'id':"exampleInputPassword"}))
# 	password2 = forms.CharField(required=True, widget=forms.PasswordInput(
# 		attrs={'placeholder': 'Repeat Password', 'class': "form-control form-control-user",
# 			   'id': "exampleRepeatPassword"}))
#
# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")
#
# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.is_staff = True
# 			user.save()
# 		return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Username', 'id': 'exampleInputEmail'}))
    password = forms.CharField(widget= forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Password',
            'id': 'exampleInputPassword',
        }))
    #remember_me = forms.BooleanField()

