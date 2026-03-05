from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.repository.repo import salva_gioco, prendi_giochi, prendi_utenti, lista_partite, aggiorna_preferito
from app.db import get_db
# from app.repository.repo import salva_gioco

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/giochi',  methods=['GET', 'POST'])
def wiew():
    if request.method == 'GET':
        GIOCHI = prendi_giochi()
        UTENTI = prendi_utenti()
        return render_template('lista_games.html', GIOCHI=GIOCHI, UTENTI=UTENTI)
    if request.method == 'POST':
        GIOCHI = prendi_giochi()
        UTENTI = prendi_utenti()

        utente_scelto = request.form["utente_scelto"]
        gioco_id = request.form["preferito"]

        aggiorna_preferito(utente_scelto,gioco_id)

        return render_template('lista_games.html',utente_scelto=utente_scelto, GIOCHI=GIOCHI, UTENTI=UTENTI)
    

@bp.route('/create', methods=['GET', 'POST'])
def create_game():
    if request.method == 'GET':
        return render_template('create_game.html')
    if request.method == 'POST':
        nome = request.form['nome']
        n_max_player = request.form['n_max_player']
        durata = request.form['durata']
        categoria = request.form['categoria']

        salva_gioco(nome, n_max_player, durata, categoria)
        return redirect(url_for('main.home'))

    return render_template('create_game.html')

@bp.route('/registra')
def registra_partita():
    if request.method == 'GET':
        return render_template('registra_partita.html')
    if request.method == 'POST':
        nome = request.form['nome']
        n_max_player = request.form['n_max_player']
        durata = request.form['durata']
        categoria = request.form['categoria']

        salva_gioco(nome, n_max_player, durata, categoria)
        return redirect(url_for('main.home'))

    return render_template('registra_partita.html')

@bp.route('/giochi/<int:id>')
def partite(id):
    partite = lista_partite(id)
    return render_template('mostra_partite.html', partite=partite)