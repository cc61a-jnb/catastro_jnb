import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from datetime import datetime
from censo.models import *
import sys
import psycopg2
import re
from datetime import *
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db import transaction
import settings

def main():
    conn = psycopg2.connect(settings.PRINCIPAL_CONNECTION_STRING)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM regiones")
    rows = cursor.fetchall()
    print len(rows)
    
if __name__ == '__main__':
    print datetime.now()
    main()
