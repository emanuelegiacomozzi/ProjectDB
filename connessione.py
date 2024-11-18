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