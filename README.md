# Python with PostgreSQL example

### Setup

1. Change content of the '.env' file with database credentials, e.g.:

FLASK_DEBUG=True
DBNAME=app
DBHOST=localhost
DBUSER=app_user
DBPASS=app_password

2. When you starting GitHub Codespace , it takes some time until all the postCreateCommand (which install the requirements.txt), in the tab terminal below, it inicates the current work. As soon its done, it will disapear and you can continue with the next step.

3. Install the libraries in the requirments.txt with following shell command:
    ```shell
    pip install -r requirements.txt
    ```


3. Make sure the Docker Containers (dpage/pgadmin4 & postgre) is running before executing following shell script in your terminal
4. Initial the migration folder
    ```shell
    python3 -m flask db init
    ```

5. Run the migrations:

    ```shell
    python3 -m flask db upgrade
    ```

### Run the example

Run the Jupyter notebook 'jupyter_postgres_db.ipynb'




### Some notes

```shell
pip install -r requirements.txt
    ```


docker system prune -f

docker container prune