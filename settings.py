# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

dotenv_path = join(dirname(r'''C:\Users\Basit\OneDrive\Summer 2019 Projects and Courses\Summer_Project_2019'''), '.env')
#print(dotenv_path)
load_dotenv(dotenv_path)

# Accessing variables.
status = os.getenv('USERNAME')
secret_key = os.getenv('PASSWORD')

# Using variables.
print(status)
print(secret_key)
