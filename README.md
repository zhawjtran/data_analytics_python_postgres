# Python with PostgreSQL example

### Setup

1. Change content of the '.env' file with database credentials, e.g.:

FLASK_DEBUG=True
DBNAME=app
DBHOST=localhost
DBUSER=app_user
DBPASS=app_password

2. When you starting GitHub Codespace , it takes some time until all the postCreateCommand (which install the requirements.txt), in the tab terminal below, it inicates the current work. As soon its done, it will disapear and you can continue with the next step.

3. Initial the migration folder
    ```shell
    python3 -m flask db init
    ```


3. Run the migrations:

    ```shell
    python3 -m flask db upgrade
    ```

### Run the example

Run the Jupyter notebook 'jupyter_postgres_db.ipynb'
