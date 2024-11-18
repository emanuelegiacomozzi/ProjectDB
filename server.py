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

def Menu():

    print("Query da eseguire:")
    print("1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?")
    print("2. Quali sono le compagnie che hanno voli che superano le 3 ore?")
    print("3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice 'CIA’ ?")
    print("4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?")
    print("5. Esci")
    
Menu()
request = input("Seleziona query da eseguire: ")
while (request != "5"):
    
        if request == "1":
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT Volo.codice, Volo.comp FROM Volo WHERE Volo.durataMinuti > 180")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except:
                print("Problemi di comunicazione con il server")

        if request == "2":
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT DISTINCT Volo.comp FROM Volo WHERE Volo.durataMinuti > 180")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except:
                print("Problemi di comunicazione con il server")

        if request == "3":
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT ArrPart.codice, ArrPart.comp FROM ArrPart WHERE ArrPart.partenza = 'CIA'")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except:
                print("Problemi di comunicazione con il server")

        if request == "4":
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT DISTINCT ArrPart.comp FROM ArrPart WHERE ArrPart.arrivo = 'FCO'")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except:
                print("Problemi di comunicazione con il server")
        
        else:
            print("Inserisci un numero valido!")
    
        Menu()
        request = input("Seleziona query da eseguire: ")