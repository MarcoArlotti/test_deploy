DROP TABLE IF EXISTS partite;
DROP TABLE IF EXISTS giochi;
DROP TABLE IF EXISTS preferiti;
DROP TABLE IF EXISTS utenti;

CREATE TABLE giochi (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  numero_giocatori_massimo INTEGER NOT NULL,
  durata_media INTEGER NOT NULL, -- durata in minuti
  categoria TEXT NOT NULL
);

CREATE TABLE utenti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL
);

CREATE TABLE preferiti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gioco_id INTEGER NOT NULL,
  utente_id INTEGER NOT NULL,
  valore BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (utente_id) REFERENCES utenti (id),
  FOREIGN KEY (gioco_id) REFERENCES giochi (id)
);

CREATE TABLE partite (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gioco_id INTEGER NOT NULL,
  data DATE NOT NULL,
  vincitore TEXT NOT NULL,
  punteggio_vincitore INTEGER NOT NULL,
  FOREIGN KEY (gioco_id) REFERENCES giochi (id)
);

-- Insert di esempio per i Giochi
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Catan', 4, 90, 'Strategia');
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Dixit', 6, 30, 'Party');
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Ticket to Ride', 5, 60, 'Strategia');

-- Insert di esempio per le Partite
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (1, '2023-10-15', 'Alice', 10);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (1, '2023-10-22', 'Bob', 12);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (2, '2023-11-05', 'Charlie', 25);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (3, '2023-11-10', 'Alice', 8);