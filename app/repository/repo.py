from app.db import get_db

def salva_gioco(nome, numero_giocatori_massimo, durata_media, categoria):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)",
            (nome, numero_giocatori_massimo, durata_media, categoria),
        )
        db.commit() # Salviamo le modifiche
        return True
    except db.IntegrityError:

        return False
    
def prendi_giochi():
    db = get_db()
    query = """
    SELECT *
    FROM giochi;
    """

    giochi = db.execute(query).fetchall()
    return [dict(gioco) for gioco in giochi]

def prendi_utenti():
    db = get_db()
    query = """
    SELECT *
    FROM utenti;
    """

    utenti = db.execute(query).fetchall()
    return [dict(utente) for utente in utenti]

def lista_partite(id):
    db = get_db()
    query = """
    SELECT *
    FROM partite
    JOIN giochi ON partite.gioco_id = giochi.id
    WHERE partite.gioco_id = ?
    ORDER BY partite.gioco_id;
    """

    partite = db.execute(query, (id,)).fetchall()
    if partite:
        return [dict(partita) for partita in partite]
    return partite

def aggiorna_preferito(utente_scelto,gioco_id):
    db = get_db()
    query = """
    SELECT 
    FROM utenti;
    """