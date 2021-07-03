# orhana-api

### **First time setup**

***Database Setup***

Download and Install PostgresSQL if not present.
- for mac os https://postgresapp.com/downloads.html
- other download page https://www.postgresql.org/download

After installing run below in plsql client command to create database
```shell
create database orhana;
```
After setting up database now let's setup project below for first time

***Project Setup***
```shell
cp orhana_api/settings-sample.py orhana_api/settings.py
python3 -m venv env

#Activate before installing dependencies
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

```
In settings.py file check and edit database configuration and add your own credentials.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "orhana",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Now having configured database connection and credentials run migration command in activated terminal (make sure env is activated)

```shell
python manage.py migrate
./populate
```

### Running in local

```shell
# To activate the environment if not activated
source env/bin/activate


# Run server

python manage.py runserver
```


### Super User

Create super user if not exists

```shell
python manage.py createsuperuser
```

To login into django admin panel go to http://localhost:8000/admin
