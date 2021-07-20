from django.shortcuts import render, redirect
from plotly.offline import plot
import plotly.graph_objects as go
from django.contrib import messages
# Create your views here.


def home(request):
    def scatter():
        #x1 = [1,2,3,4]
        #y1 = [30, 35, 25, 45]
        import pymongo
        from pymongo import MongoClient
        import ssl
        import datetime
        import pandas as pd
        from .dash_apps.finished_apps.nutrienti import dataframe_nutrimenti, calcola_nutrienti

        # Sistemare tutto
        client = pymongo.MongoClient(
            "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
            ssl_cert_reqs=ssl.CERT_NONE)
        # db = client.test
        db = client['ArmoniaBot']
        col = db['AlimentiDB']
        username = None
        if request.user.is_authenticated:
            username = request.user.email#username
            print(username)
        if(username == 'aabeltino'):
            prove = col.find({'Nome': 'AlessioNone'})
        else:
            prove = col.find({'Nome': 'GiuseppeMaulucci'})
        data = pd.DataFrame()
        for prova in prove:
            date = prova['Data']
            colazione = calcola_nutrienti(prova, 'Colazione')
            pranzo = calcola_nutrienti(prova, 'Pranzo')
            cena = calcola_nutrienti(prova, 'Cena')
            merenda = calcola_nutrienti(prova, 'Merenda')
            dff, cola, pra, cen, mere = dataframe_nutrimenti(colazione, pranzo, cena, merenda, date)
            data = data.append(dff)
        data['Data'] = data.index
        data["Data"] = pd.to_datetime(data["Data"], format="%Y-%m-%d")
        data.sort_values("Data", inplace=True)
        x1=data['Data']
        y1=data['Calorie']

        trace = go.Scatter(
            x=x1,
            y=y1
        )
        layout = dict(
            title=username,#'Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)

def login(request):
    return render(request, 'home/login.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')



from .dash_apps.finished_apps.forms import NameForm, SearchFood

#def get_name(request):
#    print('Sono entrato')
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = NameForm(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = NameForm()

#    return render(request, 'name.html', {'form': form})


def index(request):
    def e_mail_message(nome,telefono,mail, messaggio):
        import email, smtplib, ssl

        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        import pandas as pd

        from colored import fg, bg, attr
        subject = "Richiesta informazioni"
        # body = "This is an email with attachment sent from Python"

        sender_email = "armonia.amministrazione@gmail.com"

        password = 'Armonia2021!!'

        #receiver_email = "armonia." + gmail + "@gmail.com"
        receiver_email = sender_email
        body = nome + ' ha scritto:\n'+messaggio+'\nContatti:\n'+'Email: '+mail+'\nTelefono: '+telefono

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        print(fg(14) + body + attr(0))
        print('%sInviato%s' % (fg(10), attr(1)))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        #from django.core.mail import send_mail

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(form.cleaned_data['your_name'])
            #print(form.your_phone)
            #print(form.your_email)
            print(form.cleaned_data['your_message'])
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            subject = form.cleaned_data['your_name']
            phone = form.cleaned_data['your_phone']
            message = form.cleaned_data['your_message']
            sender = form.cleaned_data['your_email']
            #cc_myself = form.cleaned_data['my_cc']

            recipients = ['armonia.amministrazione@gmail.com']
            #if cc_myself:g
            #    recipients.append(sender)
            e_mail_message(subject, phone, sender, message)
            #send_mail(subject, message, sender, recipients)
            messages.success(request, 'Contact request submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    context = {
        'form' : form
    }
    #context = {
    #    'send': e_mail_message('amministrazione',message)
    #}
    return render(request, 'home/landing_page/index.html',context)

from .dash_apps.finished_apps.forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm #add this

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("welcome.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="home/landing_page/register.html", context={"register_form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("welcome.html")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="home/landing_page/login.html", context={"login_form":form})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return redirect("welcome.html")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginForm()
	return render(request=request, template_name="home/landing_page/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("login")

# def tables(request):
#     return redirect("home/landing_page/tables.html")

def form(request):
    def search(alimento):
        import pymongo
        from pymongo import MongoClient
        import ssl
        import datetime
        client = pymongo.MongoClient(
            "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
            ssl_cert_reqs=ssl.CERT_NONE)

        db = client['ArmoniaBot']
        col = db['DatabaseDietabit']
        somma = 0  # Calorie

        db2 = []
        print('Cerco in dietabit:', alimento.split()[0])
        nome = alimento.split()[0]
        query_ricerca = {"Nome": {"$regex": nome[0:len(nome) - 1]}}

        print('Ecco la lista in dietabit')
        ricette = []
        for ric in col.find(query_ricerca):
            print(ric['Nome'])
            ricette.append(ric)

        print('Cerco anche in Crea')
        col = db['DatabaseCibo']
        for ric in col.find(query_ricerca):
            print(ric['Nome'])
            ricette.append(ric)
        query_ricerca = {"Nome": {"$regex": nome[0:len(nome) - 1].lower()}}
        print('Cerco anche in BDA')
        col = db['DatabaseBDA']
        for ric in col.find(query_ricerca):
            print(ric['Nome'])
            ricette.append(ric)

        print('Cerco anche in RicetteCalorie')
        col = db['DatabaseRicetteCalorie']
        for ric in col.find(query_ricerca):
            print(ric['Nome'])
            ricette.append(ric)

        print('Cerco anche in SushiDB')
        col = db['SushiDB']
        query_ricerca = {"Name": {"$regex": nome[0:len(nome) - 1]}}
        for ric in col.find(query_ricerca):
            print(ric['Name'])
            ricette.append(ric)

        for j in range(0, len(ricette)):
            if ('Nome' in ricette[j].keys()):
                (ricette[j]['Nome'])
            else:
                (ricette[j]['Name'])
        import openfoodfacts
        ricette2 = openfoodfacts.products.get_by_brand(alimento)
        # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for j in range(0, len(ricette2)):
            ricette.append(ricette2[j])
            if ('product_name' in ricette2[j].keys()):
                (ricette2[j]['product_name'])
            elif ('product_name_en' in ricette2[j].keys()):
                (ricette2[j]['product_name_en'])
            elif ('product_name_it' in ricette2[j].keys()):
                (ricette2[j]['product_name_it'])
            elif ('product_name_fr' in ricette2[j].keys()):
                (ricette2[j]['product_name_fr'])
        alimenti=[]
        for ricetta in ricette:
            if('Nome' in ricetta.keys()):
                alimenti.append(ricetta['Nome'])
            elif ('Name' in ricetta.keys()):
                alimenti.append(ricetta['Name'])
            elif ('product_name' in ricetta.keys()):
                alimenti.append(ricetta['product_name'])
            elif ('product_name_en' in ricetta.keys()):
                alimenti.append(ricetta['product_name_en'])
            elif ('product_name_it' in ricetta.keys()):
                alimenti.append(ricetta['product_name_it'])
            elif ('product_name_fr' in ricetta.keys()):
                alimenti.append(ricetta['product_name_fr'])
        return alimenti

    def inserire(alimento, pasto, data, qty, utente):
        import pymongo
        from pymongo import MongoClient
        import ssl
        import datetime
        client = pymongo.MongoClient(
            "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
            ssl_cert_reqs=ssl.CERT_NONE)

        db = client['ArmoniaBot']
        col = db['Prova']
        col2 = db['DatabaseDietabit']
        ali = col2.find_one({'Nome': alimento})
        ali['Quantita'] = float(qty)
        dt = datetime.datetime.combine(data, datetime.datetime.min.time())
        col.insert_one({'Nome': utente, 'Data': dt, pasto: {'1': ali}})

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchFood(request.POST)
        # check whether it's valid:
        #from django.core.mail import send_mail
        insieme = []
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(form.cleaned_data['search_name'])
            nome = form.cleaned_data['search_name']
            data = form.cleaned_data['data']
            pasto = form.cleaned_data['pasto']
            qty = form.cleaned_data['qty']
            if request.user.is_authenticated:
                usern = request.user.username
            else:
                usern = ''
            insieme = []
            insieme = [nome,data,pasto,qty,usern]
            print(insieme)
            inserire(nome,pasto,data,qty,usern)
            # alimenti = search(nome)
            # for i in range(0, len(alimenti)):
            #     print(alimenti[i])
            # #send_mail(subject, message, sender, recipients)
            # ricetta =alimenti
            # ric = alimenti
            # print(len(ric))
            # ric.sort()
            # print(ric)
            # ric2=[]
            # for ri in ric:
            #     ric2.append((ri, ri))
            # from django import forms
            # class Food(forms.Form):
            #     food = forms.MultipleChoiceField(
            #         required=False,
            #         widget=forms.RadioSelect,
            #         choices=ric2,
            #     )
            # form2 = Food(request.POST)
            form = SearchFood()
            ricetta = None
            form2 = None
            insieme = []
            context = {
                'form': form,
                'insieme': insieme,
                # 'ricette' : ricetta,
                # 'form2' : form2
            }
            request.method = 'GET'
            return render(request, 'home/landing_page/tables.html', context)
            messages.success(request, 'Contact request submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('GET')
        form = SearchFood()
        ricetta = None
        form2 = None
        insieme = []

    context = {
        'form' : form,
        'insieme':insieme,
        #'ricette' : ricetta,
        #'form2' : form2
    }
    return render(request, 'home/landing_page/tables.html',context)

# from .dash_apps.finished_apps.forms import FormForm
#
# def country_form(request):
#     # instead of hardcoding a list you could make a query of a model, as long as
#     # it has a __str__() method you should be able to display it.
#     import pymongo
#     from pymongo import MongoClient
#     import ssl
#     import datetime
#     import pandas as pd
#     # Sistemare tutto
#     client = pymongo.MongoClient(
#         "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
#         ssl_cert_reqs=ssl.CERT_NONE)
#     # db = client.test
#     db = client['ArmoniaBot']
#     col = db['DatabaseDietabit']
#     lista = col.find()
#     FOOD_CHOICES = []
#     alimenti = []
#     for lis in lista:
#         alimenti.append(lis['Nome'])
#     col = db['DatabaseCibo']
#     lista = col.find()
#     #FOOD_CHOICES = []
#     #alimenti = []
#     for lis in lista:
#         alimenti.append(lis['Nome'])
#     # col = db['DatabaseBDA']
#     # lista = col.find()
#     # #FOOD_CHOICES = []
#     # #alimenti = []
#     # for lis in lista:
#     #     alimenti.append(lis['Nome'])
#     col = db['SushiDB']
#     lista = col.find()
#     #FOOD_CHOICES = []
#     #alimenti = []
#     for lis in lista:
#         alimenti.append(lis['Name'])
#     country_list = tuple(alimenti)#('Mexico', 'USA', 'China', 'France')
#     form = FormForm(data_list=country_list)
#
#     return render(request, 'home/landing_page/form.html', {
#         'form': form,
#
#     })

