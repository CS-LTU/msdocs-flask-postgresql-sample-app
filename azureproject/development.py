import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['tdgwdcmeaq'],
    dbpass=os.environ['W142H636DZKC41BY$'],
    dbhost=os.environ['msdocs-python-postgres-faz3-server.postgres.database.azure.com'],
    dbname=os.environ['msdocs-python-postgres-faz3-database']
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

