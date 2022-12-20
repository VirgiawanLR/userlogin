import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path


# dotenv_path = Path('/home/virgiawan/project/User_SignUp_SignIn/.env')
# load_dotenv(dotenv_path=dotenv_path)

load_dotenv()
mydb = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASS'),
    database = os.getenv('MYSQL_DB')
)