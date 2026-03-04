from ..db import get_db
def get_channel():
    db = get_db()
    query = """
        SELECT *
        FROM canali
        ORDER BY numero_iscritti DESC;
    """
    channels = db.execute(query).fetchall()
    print("Channels fetched from database:", channels)
    print(channels)
    return [dict(channel) for channel in channels]