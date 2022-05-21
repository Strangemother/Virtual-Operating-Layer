"""Generate the KV.
"""
# import django
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'header.settings')
from django.core.management import execute_from_command_line

execute_from_command_line(['manage.py', 'makemigrations'])
execute_from_command_line(['manage.py', 'migrate'])

# django.setup()

# from header import models

# kv = models.KeyValue()
