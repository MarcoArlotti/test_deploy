from ..db import get_db
def get_categorie():
    db = get_db()
    query = """
        SELECT categoria.id, categoria.nome
        FROM categoria
        ORDER BY categoria.nome ASC;
    """
    file = db.execute(query).fetchall()

    lista_categorie =  []
    for fila in file:
        categoria = { 
            "id": fila["id"], 
            "nome": fila["nome"] 
            }
        print(categoria)
        lista_categorie.append(categoria)
    print("categorie fetched from database:", lista_categorie)
    return lista_categorie