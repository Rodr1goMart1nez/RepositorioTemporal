import pyodbc
from django.conf import settings
import os
import django

# Setup Django environment manually effectively just to get settings if needed, 
# but here I'll just use the raw connection string since I know it working from check_db.py

server = r'(localdb)\SERVIDOR'
user = 'Prueba'
password = '1234567'
database = 'servidor'
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};UID={user};PWD={password};DATABASE={database};TrustServerCertificate=yes;'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    fields_to_check = [
        'IMPACTO', 
        'BLOQUEO_CANAL', 
        'BLOQUEO_TC_TD', 
        'BLOQUEO_FONDO', 
        'BLOQUEO_OTRO',
        'STATUS_ID',
        'PRIORITY_ID'
    ]

    for field in fields_to_check:
        print(f"--- DISTINCT VALUES FOR {field} ---")
        try:
            cursor.execute(f"SELECT DISTINCT {field} FROM WALLE_BPM")
            rows = cursor.fetchall()
            values = [row[0] for row in rows if row[0] is not None]
            print(values)
        except Exception as e:
            print(f"Error fetching {field}: {e}")

    conn.close()

except Exception as e:
    print(f"Error connecting: {e}")
