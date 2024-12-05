import sys,requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

base_url = "http://127.0.0.1:5001"

def get_response(endpoint, params=None):
    try:
        if params:
                response = requests.get(f"{base_url}{endpoint}", params=params)
        else:
            response = requests.get(f"{base_url}{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def Menu():

    print()
    print("Operazioni disponibili:")
    print()
    print("1. Visualizza voli disponibili")
    print("2. Visualizza i voli delle compagnie")
    print("3. Visualizza gli aeroporti che effettuano voli")
    print("4. Visualizza gli aeroporti di arrivo e quelli di partenza")
    print("5. Visualizza il luogo degli aeroporti ")
    print("6. Esci")
    
def main():
    while True:
        Menu()
        request = input("Seleziona operazione da eseguire: ")
        if request == "1":
            results = get_response("/voli")
            for row in results:
                print(row)
        elif request == "2":
            results = get_response("/compagnie_voli")
            for row in results:
                print(row)
        elif request == "3":
            results = get_response("/aeroporti")
            for row in results:
                print(row)
        elif request == "4":
            results = get_response("/aeroporti_part_arr")
            for row in results:
                print(row)
        elif request == "5":
            results = get_response("/luogo_aeroporti")
            for row in results:
                print(row)
        elif request == "6":
            print("Esci...")
            break
        else:
            print("Inserisci un numero valido!")

if __name__ == "__main__":
    main()