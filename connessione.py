import psycopg2

host = "localhost"
port = "5432"
dbname="Cielo"
user="postgres"
password="postgres"

try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Connessione al database avvenuta con successo")
except Exception as e:
    print(f"Errore durante la connessione al database: {e}")

def Cursor():
    print("Query: ")
    print()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM volo\n")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

    cursor2 = connection.cursor()
    cursor2.execute("SELECT * FROM luogoaeroporto WHERE citta='Roma'")
    rows2 = cursor2.fetchall()
    for row in rows2:
        print(row)
    print()

    cursor3 = connection.cursor()
    cursor3.execute("SELECT partenza FROM arrpart")
    rows3 = cursor3.fetchall()
    for row in rows3:
        print(row)
    print()
    
Cursor()

