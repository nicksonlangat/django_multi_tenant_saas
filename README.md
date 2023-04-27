## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)

## Installing
### Setting up the database
- Start your database server and create your database

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/nicksonlangat/django_multi_tenant_saas.git) `git clone https://github.com/nicksonlangat/django_multi_tenant_saas.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment` and activate it `source name_of_your_virtual_environment/bin/activate`
- Create a .env file in root directory and put these key=values in it:
```
DEBUG=on
SECRET_KEY='your secret key'
DB_NAME="your_db_name"
DB_USER="your_postgres_username"
DB_PASSWORD="your_postgres_password"
DB_PORT="your_postgres_port"
DB_HOST="localhost or any other host name"
```
- Use https://djecrety.ir/ to generate secret key
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate_schemas --shared`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Create the default public domain by running `python manage.py create_public_domain`
- Edit your hosts file by adding the default domain `buupass.local` by mapping it to `127.0.0.1`
- Run the server `python manage.py runserver`
- Visit `buupass.local:8000` to view the app. Create a tenant by visiting `buupass.local:8000/clients/`
- Edit your hosts file by adding the tenant domain `subdomain.buupass.local` by mapping it to `127.0.0.1`
- You can now visit the subdomain and add users.
