# Python with PostgreSQL example

### Setup

1. Change content of the '.env' file with database credentials, e.g.:

FLASK_DEBUG=True
DBNAME=app
DBHOST=localhost
DBUSER=app_user
DBPASS=app_password

2. Install the libraries in the requirments.txt with following shell command:
    ```shell
    pip install -r requirements.txt
    ```


3. Make sure the Docker Containers (dpage/pgadmin4 & postgre) is running before executing following shell script in your terminal
    ```shell
    docker compose up -d
    ```

### Run the example
Run the Jupyter notebook 'jupyter_postgres_db.ipynb'

### Run the Flask app
python3 app.py


### pgAdmin settings
1. Dashboard: Quick Links: Add New Server
2. Tab General:
    Name: Postgres_DB
3. Tab Connection:
    Host name/address:  db
    Port: 5432
    Usrename: app_user
    Password: app_password
    Save password? Yes 


### Some notes
docker system prune -f

docker container prune