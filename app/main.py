# app/main.py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import post_db
from app.repository.canali_repositories import get_channel
from app.repository.video_repositories import get_videos
from app.repository.categorie import get_categorie

bp = Blueprint('main', __name__)

@bp.route('/channel')
def index():
    channels_py = get_channel()
    return render_template("stampa_canali.html", channels_html=channels_py)

@bp.route('/channel/<int:canale_id>')
def channel(canale_id):
    video_py = get_videos(canale_id)
    return render_template("channel.html",videos_html=video_py)

@bp.route('/create_channel', methods=['GET','POST'])
def create_channel():
    if request.method == 'GET':
        categorie_py:list = get_categorie()
        return render_template('create_channel.html', lista_categorie=categorie_py)
    
    if request.method == 'POST':
        categoria_id = request.form.get('categoria_id')
        nome = request.form.get('nome')
        numero_iscritti = request.form.get('numero_iscritti')

        query = """ INSERT INTO canali (nome, numero_iscritti, categoria_id) VALUES (?, ?, ?) """
        post_db(query, (nome,numero_iscritti,categoria_id))
        categorie_py = get_categorie()



        return render_template('create_channel.html', lista_categorie=categorie_py)
