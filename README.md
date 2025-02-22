# ProjectDB

# L'applicazione permette di visualizzare informazioni specifiche sui voli, compagnie aeree e aeroporti ,recuperate da un database chiamato Cielo. Questi dati sono esposti tramite un'API REST, gestita all'interno del file app.py.
# Per quanto riguarda il lato frontend,l'applicazione è stata sviluppata utilizzando React. L'applicazione è stata progettata per essere responsive, permettendo di adattarsi a più dispositivi di diverse dimensioni.

# Funzionalità principali

# 1.Visualizzazione delle informazioni
   # Voli: consente di visualizzare il codice dei voli, il nome della compagnia e la durata in minuti.
   # Compagnie aeree: visualizza il nome delle compagnie aeree e l'anno di fondazione.
   # Aeroporti: visualizza il nome, il codice, la città e la nazione degli aeroporti

# 2.Navigazione
   # Header e Navbar: l'applicazione offre una navigazione semplice tra le pagine con un header fisso, che include il nome dell'agenzia, il logo e un link di ritorno verso la Home page. La barra di navigazione invece mette a disposizione dei link diretti alle varie sezioni dell'applicazione(Voli,Compagnie Aeree, Aeroporti)
   # Home Page: pagina principale dell'applicazione che offre una breve introduzione dell'agenzia di viaggi con un messaggio di benvenuto.

# 3.Interazione con l'API
   # L'applicazione interagisce con l'API REST del backend app.py per il recupero dei dati. Le richieste ai servizi vengono effettuate in modo asincrono utilizzando Axios, un client HTTP. I dati ottenuti vengono poi gestiti nei file Voli, Compagnie e Aeroporti e visualizzati in tabelle. Il backend è ospitato localmente, con indirizzo IP localhost e porta 5002.


# Istruzioni per utilizzare l'applicazione

# aprire il terminale 
   # git clone https://github.com/emanuelegiacomozzi/ProjectDB.git (clona repository)
   # cd ProjectDB (sposta nella repository clonata contentente app.py e l'applicazione test-react)
   # npm install (installa le dipendenze)
   # Node -v , Npm -v (verifica le versioni di node e npm)  
# aprire il terminale in vscode
   # python (o python3 a seconda della versione) app.py(per runnare il server)
   # se non sono riconosciute le seguenti librerie , installare : 
   # pip intall Flask
   # pip install psycopg2
   # pip install flask-cors
# aprire un secondo terminale in vscode:
   # cd test-react(sposta nella directory contenente l'applicazione in react)
   # npm run dev (per avviare l'applicazione)
