from flask import Flask, jsonify
import sys  
import psycopg2
import urllib3
from flask_cors import CORS

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

CORS(app)


host = "localhost"
port = "5432"
dbname="Cielo"
user="postgres"
password="postgres"

def dbconnect():
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        print("Connessione al database avvenuta con successo")
        return connection
    except Exception as e:
        print(f"Errore durante la connessione al database: {e}")
        raise

@app.route('/api/voli', methods=['GET'])
def GestisciVoli():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT v.codice, v.comp, v.durataminuti FROM Volo v")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}")
        return jsonify({"error": "Errore durante la comunicazione con il database", "details": str(e)}), 500

@app.route('/api/compagnie_voli', methods=['GET'])
def GestisciCompagnieVoli():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT nome,annoFondaz FROM Compagnia ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500


@app.route('/api/aeroporti', methods=['GET'])
def GestisciAeroportiPartArr():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT a.codice,a.nome,la.citta,la.nazione from LuogoAeroporto la, Aeroporto a where la.aeroporto = a.codice ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

if __name__=='__main__':
    app.run(debug=True, port=5002)

