import sqlite3
import os

# Definiamo dove creare il file del database (nella cartella instance)
if not os.path.exists('app/instance'):
    os.makedirs('app/instance')

db_path = os.path.join('app/instance', 'database.sqlite')

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open('app/database.sql') as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()