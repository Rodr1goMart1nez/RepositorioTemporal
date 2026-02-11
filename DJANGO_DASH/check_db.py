import pyodbc

server = r'(localdb)\SERVIDOR'
user = 'Prueba'
password = '1234567'
try:
    driver_names = [x for x in pyodbc.drivers() if 'SQL Server' in x]
    print(f"Drivers disponibles: {driver_names}")
    
    # Priorizar ODBC Driver 17/18 si existe, sino SQL Server nativo
    driver = None
    for d in ['ODBC Driver 17 for SQL Server', 'ODBC Driver 18 for SQL Server', 'SQL Server']:
        if d in driver_names:
            driver = "{" + d + "}"
            break
    if not driver and driver_names:
        driver = "{" + driver_names[0] + "}"
    elif not driver:
         driver = '{SQL Server}'

    print(f"Usando driver: {driver}")

    found_db = None

    conn_str = f'DRIVER={driver};SERVER={server};UID={user};PWD={password};DATABASE=master;TrustServerCertificate=yes;'
    print(f"Intentando conectar a master con: {conn_str}")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Listar DBs
    cursor.execute("SELECT name FROM sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')")
    databases = [row[0] for row in cursor.fetchall()]
    conn.close()

    print(f"Bases de datos encontradas: {databases}")

    for db in databases:
        try:
            conn_str_db = f'DRIVER={driver};SERVER={server};UID={user};PWD={password};DATABASE={db};TrustServerCertificate=yes;'
            conn_db = pyodbc.connect(conn_str_db)
            cursor_db = conn_db.cursor()
            cursor_db.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'WALLE_BPM'")
            if cursor_db.fetchone():
                found_db = db
                print(f"Tabla WALLE_BPM encontrada en base de datos: {db}")
                conn_db.close()
                break
            conn_db.close()
        except Exception as e:
            print(f"Error accediendo a {db}: {e}")

except Exception as e:
    print(f"Error general: {e}")

if found_db:
    print(f"FOUND_DB: {found_db}")
else:
    print("No se encontró la tabla en ninguna DB accesible.")
