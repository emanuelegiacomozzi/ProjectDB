from flask import Flask, jsonify
import sys  
import psycopg2
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

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

@app.route('/')
def home():
    return """
    <h1> Benvenuto sul sito della nostra agenzia di viaggi!</h1>
    <p> Voli disponibili : <a href='/api/voli'>clicca qui</a></p>
    <p> Voli delle rispettive compagnie :<a href = '/api/compagnie_voli'>clicca qui</a></p>
    <p> Aeroporti che effettuano voli :<a href = '/api/aeroporti'>clicca qui</a></p>
    <p> Aeroporti di partenza e arrivo :<a href = '/api/aeroporti_arr_part'>clicca qui</a></p>
    <p> Luogo degli aeroporti :<a href = '/api/luogo_aeroporti'>clicca qui</a></p>
    """

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
        cursor.execute("SELECT * FROM Compagnia c, Volo v WHERE c.nome = v.comp ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

@app.route('/api/aeroporti', methods=['GET'])
def GestisciAeroporti():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aeroporto ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

@app.route('/api/aeroporti_arr_part', methods=['GET'])
def GestisciAeroportiPartArr():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ArrPart ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

@app.route('/api/luogo_aeroporti', methods=['GET'])
def GestisciLuogoAeroporti():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LuogoAeroporto ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

if __name__=='__main__':
    app.run(port=5001)

