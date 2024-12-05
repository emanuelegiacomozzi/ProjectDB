from flask import Flask, request , jsonify
import sys  
import psycopg2

api = Flask(__name__)

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
        sys.exit()

@api.route('/voli', methods=['GET'])
def GestisciVoli():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Volo")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500


@api.route('/compagnie_voli', methods=['GET'])
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

@api.route('/aeroporti', methods=['GET'])
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

@api.route('/aeroporti_part_arr', methods=['GET'])
def GestisciAeroportiPartArr():
    try:
        conn = dbconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT ap.partenza, ap.arrivo FROM ArrPart ap ")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        print(f"Problemi di comunicazione con il server {e}"), 500

@api.route('/luogo_aeroporti', methods=['GET'])
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
        print(f"Problemi di comunicazione con il server {e}"), 

if __name__ == '__main__':
    api.run(debug=True, port=5001)

