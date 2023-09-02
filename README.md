
![Currency](https://github.com/PioBuczek/CurrencyWallet/assets/137912290/43ff1188-fd81-4753-8372-d3ed794be642)

### A few words about project
This project, is a currency wallet, which show actual amount of your currencies and balance which is show in PLN currency. On the main page there is a list of the currency and their price. In this application, you could add new positions and substract previous positions. Moreover, as you add another item to your portfolio, a pie chart is generated that shows the percentage composition of your portfolio.

### How start this application ?

Before we start, you need to create a database(This project is used PostgreSQL version 15). You need to know, that this project was tested in Postgres, but if you want to use a different database you need to configure settings accordingly.

Firstly, you need to clone my repo to my GitHub, and you need to use commande: 
<div class="termy">

```console
git clone https://github.com/PioBuczek/CurrencyWallet.git
```
</div> 

Then you need to go into a higher file, you need the command:
<div class="termy">

```console
cd CryptoWalletPython
```
</div> 

Second, you need to change this settings. In the tree, click on "settings" and find DATABASE, and change this data:

<div class="termy">

```console
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "{{NAME}}",
        "USER": "{{USER}}",
        "PASSWORD": "{{PASSWORD}}",
        "HOST": "{{HOST}}",
        "PORT": "{{PORT}}",
    },
}

```
</div> 

Next, you need to create of virtual environments (venv). In the terminal, write the command that will create your venv and install library which are necessery:
<div class="termy">

```console
python -m venv YourVenv
./YourVenv/Scripts/activate.ps1
pip install -r requirements.txt  
```
</div> 

If after this command you will get error, you need to open Windows PowerShell and you need to write command: 

<div class="termy">

```console
Set-ExecutionPolicy RemoteSigned 
```
</div> 


### Run it
You need to generate migration files for the models defined in application. The migration files contain the changes to the database schema to be applied.


<div class="termy">

```console
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
</div>


The development server will start,at
<div class="termy">

```console
http://localhost:8000/
```
</div>
  in browser.
