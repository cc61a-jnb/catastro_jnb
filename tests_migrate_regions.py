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

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def main():
    conn_string = "host='127.0.0.1' dbname='mydb' port='5432' user='cc61a' password='cc61a'"
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usu_cargo")
    rows = cursor.fetchall()
    len_rows = len(rows)
    
    profiles = UserProfile.objects.order_by('old_id')
    profile_ids = [p.old_id for p in profiles]
    
    roles = Role.objects.order_by('old_id')
    role_ids = [p.old_id for p in roles]
    
    cuerpos = Cuerpo.objects.order_by('old_id')
    cuerpo_ids = [p.old_id for p in cuerpos]
    
    counter = 0;
    
    for idx, row in enumerate(rows):
        try:
            old_id = int(row[2])
            if binary_search(profile_ids, old_id) == -1:
                counter += 1
                continue
        except TypeError, e:
            counter += 1
            continue
            
        try:
            old_id = int(row[1])
            if binary_search(role_ids, old_id) == -1:
                counter += 1
                continue
        except TypeError, e:
            counter += 1
            continue
            
        try:
            old_id = int(row[4])
            if binary_search(cuerpo_ids, old_id) == -1:
                counter += 1
                continue
        except TypeError, e:
            counter += 1
            continue
        
    print counter

if __name__ == '__main__':
    print datetime.now()
    main()
   

